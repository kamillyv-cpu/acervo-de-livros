from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Autor, Genero, Livro


def listar_livros(request):
    # 1. Recuperar parâmetros do GET
    busca = request.GET.get('q', '').strip()
    autor_id = request.GET.get('autor', '')
    genero_id = request.GET.get('genero', '')

    # 2. Consulta base (select_related evita consultas extras por livro)
    livros = Livro.objects.select_related('autor', 'genero')

    # 3. Aplicar pesquisa e filtros ANTES da paginação
    if busca:
        livros = livros.filter(titulo__icontains=busca)

    if autor_id.isdigit():
        livros = livros.filter(autor_id=autor_id)

    if genero_id.isdigit():
        livros = livros.filter(genero_id=genero_id)

    # 4. Paginação: 5 por página
    paginator = Paginator(livros, 5)
    page_obj = paginator.get_page(request.GET.get('page'))

    # 5. Query string sem o "page", para preservar filtros nos links
    params = request.GET.copy()
    params.pop('page', None)
    query_string = params.urlencode()

    contexto = {
        'page_obj': page_obj,
        'paginator': paginator,
        'autores': Autor.objects.all(),
        'generos': Genero.objects.all(),
        'busca': busca,
        'autor_selecionado': autor_id,
        'genero_selecionado': genero_id,
        'query_string': query_string,
    }
    return render(request, 'catalogo/listar_livros.html', contexto)
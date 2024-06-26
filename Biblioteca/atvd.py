import json

# Classe Documento
class Documento:
    def __init__(doc, titulo, data, tema, contexto, descricao, autor, localizacao, materiais_relacionados=None, figura_historica=None):
        doc.titulo = titulo
        doc.data = data
        doc.tema = tema
        doc.contexto = contexto
        doc.descricao = descricao
        doc.autor = autor
        doc.localizacao = localizacao
        doc.materiais_relacionados = materiais_relacionados if materiais_relacionados else []
        doc.figura_historica = figura_historica

    def to_dict(doc):
        return {
            "titulo": doc.titulo,
            "data": doc.data,
            "tema": doc.tema,
            "contexto": doc.contexto,
            "descricao": doc.descricao,
            "autor": doc.autor,
            "localizacao": doc.localizacao,
            "materiais_relacionados": doc.materiais_relacionados,
            "figura_historica": doc.figura_historica
        }

class Autor:
    def __init__(autor, nome, data_nascimento, local_nascimento, biografia, areas_pesquisa):
        autor.nome = nome
        autor.data_nascimento = data_nascimento
        autor.local_nascimento = local_nascimento
        autor.biografia = biografia
        autor.areas_pesquisa = areas_pesquisa

    def to_dict(autor):
        return {
            "nome": autor.nome,
            "data_nascimento": autor.data_nascimento,
            "local_nascimento": autor.local_nascimento,
            "biografia": autor.biografia,
            "areas_pesquisa": autor.areas_pesquisa
        }

class AreaPesquisa:
    def __init__(area, denominacao, periodo_estudo, caracteristicas, obras_principais):
        area.denominacao = denominacao
        area.periodo_estudo = periodo_estudo
        area.caracteristicas = caracteristicas
        area.obras_principais = obras_principais

    def to_dict(area):
        return {
            "denominacao": area.denominacao,
            "periodo_estudo": area.periodo_estudo,
            "caracteristicas": area.caracteristicas,
            "obras_principais": area.obras_principais
        }

def ordenar_por_titulo(documentos):
    return sorted(documentos, key=lambda doc: doc.titulo)

def salvar_em_arquivo(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_de_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return json.load(f)

if __name__ == "__main__":

    autor1 = Autor("João Silva", "1975-03-12", "Porto Alegre", "Historiador especializado em Idade Média.", ["Idade Média", "História da Europa"])
    autor2 = Autor("Maria Santos", "1982-07-21", "São Paulo", "Historiadora de arte contemporânea.", ["Arte Contemporânea", "História da Cultura"])
    
    area1 = AreaPesquisa("Idade Média", "500-1500 d.C.", "Período marcado por feudalismo e cruzadas.", ["Decadência e Queda do Império Romano", "O Papado na Idade Média"])
    area2 = AreaPesquisa("Arte Contemporânea", "Século XX - XXI", "Movimentos como surrealismo e expressionismo.", ["Guernica de Pablo Picasso", "A Persistência da Memória de Salvador Dalí"])

    doc1 = Documento("Decadência e Queda do Império Romano", "476 d.C.", "História Antiga", "Fim do Império Romano do Ocidente.", "Análise sobre os fatores que levaram à queda do Império Romano.", autor1.nome, "Prateleira A1")
    doc2 = Documento("Guernica de Picasso", "1937", "Arte", "Pintura de Pablo Picasso durante a Guerra Civil Espanhola.", "Análise da pintura Guernica e seu impacto cultural e político.", autor2.nome, "Prateleira B2")

    documentos = [doc1, doc2]
    documentos_ordenados = ordenar_por_titulo(documentos)

    dados_para_salvar = {"documentos": [doc.to_dict() for doc in documentos_ordenados]}
    salvar_em_arquivo(dados_para_salvar, "biblioteca_historia.json")

    dados_carregados = carregar_de_arquivo("biblioteca_historia.json")
    documentos_carregados = [Documento(**doc) for doc in dados_carregados["documentos"]]

    for doc in documentos_carregados:
        print(f"Título: {doc.titulo}, Autor: {doc.autor}, Data: {doc.data}, Localização: {doc.localizacao}")


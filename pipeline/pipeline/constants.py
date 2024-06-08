from enum import Enum
class constants(Enum):
    """
    Enum class that represents a collection of constants used in the pipeline.
    """
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    INPUT = '/home/tricktx/project_pipeline_anp/download_files/'
    
    OUTPUT = '/home/tricktx/project_pipeline_anp/output/'
    
    URLS = [
            "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-glp.csv",
            "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-gasolina-etanol.csv",
            "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-diesel-gnv.csv",
        ]
    
    PATH = [
        INPUT + 'ultimas-4-semanas-glp.csv',
        INPUT + 'ultimas-4-semanas-gasolina-etanol.csv',
        INPUT + 'ultimas-4-semanas-diesel-gnv.csv'
        ]
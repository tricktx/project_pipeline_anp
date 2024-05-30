from enum import Enum
class constants(Enum):
    """
    Enum class that represents a collection of constants used in the pipeline.
    """

    INPUT = '/tmp/anp/input/'
    
    OUTPUT = '/tmp/anp/output/'
    
    URLS = [
            "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-glp.csv",
            "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-gasolina-etanol.csv",
            "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-diesel-gnv.csv",
        ]
    
    path = [
        INPUT + 'ultimas-4-semanas-glp.csv',
        INPUT + 'ultimas-4-semanas-gasolina-etanol.csv',
        INPUT + 'ultimas-4-semanas-diesel-gnv.csv'
        ]
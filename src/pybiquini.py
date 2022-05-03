import requests
from bs4 import BeautifulSoup
import pandas as pd

class Clientapibiquini:
    """
    Cliente de API para consumir a melhor API do Biquini Cavadão
    """
    def get_shows(country = "", state = "", city = ""):
        """
        Obtêm o histórico de shows da banda Biquini Cavadão

        :param country: string País em que se deseja obter o histórico de shows
        :param state: string Sigla do estado em que se deseja obter o histórico de shows
        :param city: string Cidade em que se deseja obter o histórico de shows

        Nenhum dos parâmetros são obrigatórios. Se não for informado
        nenhum dos parâmetros será baixado todo o histórico de shows

        :return Retorna um data.frame com o histórico dos shows da banda segundo os parâmetros especificados
        """
        resp = requests.get("https://api-biquini.herokuapp.com/shows?"+"pais="+country+"&estado="+state+"&cidade="+city)
        shows = pd.read_json(resp.text)
        return shows
    
    def get_musics(album):
        """
        Retorna a lista de músicas contidas em um album

        :param album: string Nome do album em que deseja consultar a lista de músicas

        :return Retorna um vetor contendo o nome das músicas do album especificado
        """
        musics = requests.get("https://api-biquini.herokuapp.com/musicas?album="+album)
        return musics.text
    
    def get_albuns_info(album = ""):
        """
        Obtêm informações dos albuns do Biquini Cavadão

        :param album: string Nome do album. Caso não seja fornecido o nome do album, serão retornadas informações
        de todos os albuns da banda.

        :return Retorna um data.frame com as informações do específico ou dos albuns.
        """
        resp = requests.get("https://api-biquini.herokuapp.com/albuns?album="+album)
        info_albuns = pd.read_json(resp.text)
        return info_albuns
    
    def get_lyrics(album, music):
        """
        Obtêm a letra da música e do album especificado

        :param album: string Nome do album que contém a música desejada
        :param musica: string Nome da música desejada

        :return Retorna a letra da música em formato HTML
        """
        resp = requests.get("https://api-biquini.herokuapp.com/letra?album="+album+"&musica="+music)
        return BeautifulSoup(resp.content, "html.parser")

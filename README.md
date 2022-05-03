pybinquini
==========

> Cliente de API para consumo das informações da banda Biquini Cavadão
> desenvolvida em Python para consumir informações estruturadas da
> banda.

------------------------------------------------------------------------

Por exemplo, para obter a letra de uma música específica pode-se rodar o
seguinte código:

    from pybiquini import Clientapibiquini

    roda_gigante = Clientapibiquini.get_lyrics(album="Roda Gigante", music="Roda-Gigante")

    print(roda_gigante)

Para obter as informações sobre os albuns:

    albuns_info = Clientapibiquini.get_albuns_info()
    print(albuns_info)

Para obter as músicas de um album específico:

    musics = Clientapibiquini.get_musics(album="Ilustre Guerreiro")
    print(musics)

Para obter o histórico de shows em determinado local a nível de país,
estado ou cidade:

    shows = Clientapibiquini.get_shows(country="Brasil", state="MT")
    print(shows)

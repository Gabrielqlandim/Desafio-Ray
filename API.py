from googleapiclient.discovery import build
import pandas as pd

#nessa linha de codigo abaixo vc vai colocar a chave API do google

API = "AIzaSyDO_tt98D6XkevbMcQBpE8w1mbpzvujN2s"

#ID da playlist da Formula 1
playlist = "PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR"

youtube = build("youtube", "v3", developerKey = API)

def get_infos(playlist):
    videos = []
    prox_video = None

    while True:
        #Aqui busca os videos na playlist
        playlist_resultado = youtube.playlistItems().list(
            part = "snippet",
            playlistId = playlist,
            maxResults = 30,
            pageToken = prox_video
        ).execute()

        for item in playlist_resultado['items']:
            idVideo = item['snippet']['resourceId']['videoId']
            titulo = item['snippet']['title']
            dataPublicacao = item['snippet']['publishedAt']

            # mais detalhes do video
            detalhesVideo = youtube.videos().list(
                part = "statistics",
                id = idVideo
            ).execute()

            status = detalhesVideo['items'][0]['statistics']
            views = int(status.get("viewCount", 0))
            likes = int(status.get("likeCount", 0))
            comentarios = int(status.get("commentCount", 0))

            #adicionar dados no dicionario videos

            videos.append({
                "titulo": titulo,
                "idVideo": idVideo,
                "views": views,
                "likes": likes,
                "Comentarios": comentarios,
                "Data de publicacao": dataPublicacao
            })

        #isso so verifica se tem mais videos para serem verificados
        prox_video = playlist_resultado.get("nextPageToken")
        if not prox_video:
            break
    
    return videos

#estruturar os videos em um DF

videos = get_infos(playlist)
df = pd.DataFrame(videos)

#exibe as informações de cada video
for index, row in df.iterrows():
    print(f"Nome: {row['titulo']}")
    print(f"Data de lancamento: {row['Data de publicacao']}")
    print(f"Comentarios: {row['Comentarios']}")
    print(f"Visualizacoes: {row['views']}")
    print(f"Curtidas: {row['likes']}")
    print(f"ID do Video: {row['idVideo']}")
    print("-" * 50)

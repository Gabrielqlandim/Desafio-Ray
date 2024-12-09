from googleapiclient.discovery import build
import pandas as pd

# Na linha de código abaixo, você vai colocar a chave da API do Google
API = "AIzaSyDO_tt98D6XkevbMcQBpE8w1mbpzvujN2s"

# ID da playlist da Fórmula 1
playlist = "PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR"

youtube = build("youtube", "v3", developerKey=API)

def get_infos(playlist):
    videos = []
    prox_video = None

    while True:
        # Aqui busca os vídeos na playlist
        playlist_resultado = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist,
            maxResults=30,
            pageToken=prox_video
        ).execute()

        for item in playlist_resultado['items']:
            id_video = item['snippet']['resourceId']['videoId']
            titulo = item['snippet']['title']
            data_publicacao = item['snippet']['publishedAt']

            # Mais detalhes do vídeo
            detalhes_video = youtube.videos().list(
                part="statistics",
                id=id_video
            ).execute()

            status = detalhes_video['items'][0]['statistics']
            visualizacoes = int(status.get("viewCount", 0))
            curtidas = int(status.get("likeCount", 0))
            comentarios = int(status.get("commentCount", 0))

            # Adicionar dados no dicionário videos
            videos.append({
                "Titulo do Video": titulo,
                "ID do Video": id_video,
                "Visualizacoes": visualizacoes,
                "Curtidas": curtidas,
                "Comentarios": comentarios,
                "Data de Publicacao": data_publicacao
            })

        # Isso verifica se há mais vídeos para serem verificados
        prox_video = playlist_resultado.get("nextPageToken")
        if not prox_video:
            break

    return videos

# Aqui coleto as informações dos vídeos
videos = get_infos(playlist)
df = pd.DataFrame(videos)

# Nome do arquivo Excel que vou salvar os dados
nome_arquivo = "dashboard_formula_1.xlsx"

# Criação do arquivo Excel com XlsxWriter
with pd.ExcelWriter(nome_arquivo, engine='xlsxwriter') as escritor:
    # Salvar os dados na planilha
    df.to_excel(escritor, sheet_name="Dados", index=False, startrow=1)

    # Acesso à planilha criada
    planilha = escritor.sheets["Dados"]

    # Criar objetos de formato de células
    formato_numero = escritor.book.add_format({'num_format': '#,##0'})  # Formato os numeros para separar os "Milhar"
    formato_data = escritor.book.add_format({'num_format': 'yyyy-mm-dd'})  # Formato a data aqui
    formato_titulo = escritor.book.add_format({'bold': True, 'font_size': 12, 'align': 'center', 'valign': 'vcenter', 'bg_color': '#B7B7B7'})

    # Definir a largura das colunas
    planilha.set_column('A:A', 30)  # Aqui é o título do vídeo
    planilha.set_column('B:B', 15)  # Aqui é o ID do vídeo
    planilha.set_column('C:C', 15, formato_numero)  # Aqui são as visualizações
    planilha.set_column('D:D', 15, formato_numero)  # Aqui são as curtidas
    planilha.set_column('E:E', 20, formato_numero)  # Aqui são os Comentários
    planilha.set_column('F:F', 20, formato_data)  # Aqui é a data de publicação

    # Inserir os títulos das colunas com a formatação devida
    planilha.write('A1', 'Titulo do Video', formato_titulo)
    planilha.write('B1', 'ID do Video', formato_titulo)
    planilha.write('C1', 'Visualizacoes', formato_titulo)
    planilha.write('D1', 'Curtidas', formato_titulo)
    planilha.write('E1', 'Comentarios', formato_titulo)
    planilha.write('F1', 'Data de Publicacao', formato_titulo)

    # Adicionar um título na planilha acima de todas as colunas
    planilha.merge_range('A1:F1', 'Dashboard de Vídeos da Fórmula 1', escritor.book.add_format({'bold': True, 'font_size': 16, 'align': 'center'}))

    # Gráfico de Visualizações por Vídeo
    grafico_visualizacoes = escritor.book.add_chart({'type': 'column'})
    grafico_visualizacoes.add_series({
        'name': 'Visualizações',
        'categories': '=Dados!$A$2:$A${}'.format(len(df) + 1),
        'values': '=Dados!$C$2:$C${}'.format(len(df) + 1),
    })
    grafico_visualizacoes.set_title({'name': 'Visualizações por Vídeo'})
    grafico_visualizacoes.set_style(11)  # Adiciona um estilo ao gráfico de video
    planilha.insert_chart('H2', grafico_visualizacoes)

    # Gráfico de Curtidas por Vídeo
    grafico_curtidas = escritor.book.add_chart({'type': 'column'})
    grafico_curtidas.add_series({
        'name': 'Curtidas',
        'categories': '=Dados!$A$2:$A${}'.format(len(df) + 1),
        'values': '=Dados!$D$2:$D${}'.format(len(df) + 1),
    })
    grafico_curtidas.set_title({'name': 'Curtidas por Vídeo'})
    grafico_curtidas.set_style(12)  # Adiciona um outro estilo diferente para o gráfico de curtidas
    planilha.insert_chart('H20', grafico_curtidas)

print(f"Dashboard salvo como {nome_arquivo}")
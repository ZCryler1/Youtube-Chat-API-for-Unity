import socket
import json
from chat_downloader import ChatDownloader

YOUTUBE_LIVE_URL = "https://youtube.com/live/URL_DA_LIVE"

# Configura o servidor para escutar na porta 5001
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5001))  # Porta 5001
server.listen(5)

print("Servidor TCP esperando conexão...")

def handle_client(conn):
    """Função para lidar com o chat e enviar mensagens para o cliente"""
    chat = ChatDownloader().get_chat(YOUTUBE_LIVE_URL)

    try:
        while True:
            message = next(chat)
            if "message" in message:
                text = message["message"]
                sender = message["author"]["name"]

                # Se a mensagem contiver palavras-chave, envia para o Unity
                if "TNT" in text.upper() or "GRANDE" in text.upper() or "RÁPIDO" in text.upper() or "PEDRA" in text.upper() or "FERRO" in text.upper() or "DIAMANTE" in text.upper() or "OURO" in text.upper() or "MADEIRA" in text.upper() or "NETHERITA" in text.upper():
                    data = {
                        "author": sender,
                        "message": text
                    }
                    conn.send(json.dumps(data).encode() + b"\n")
                    print(f"Enviando para o Unity: {data}")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        conn.close()  # Fecha a conexão quando terminar ou ocorrer um erro

# Loop para aceitar novas conexões continuamente
while True:
    try:
        conn, addr = server.accept()
        print(f"Conectado por {addr}")

        # Cria uma nova thread ou começa a manipular a conexão
        handle_client(conn)

    except Exception as e:
        print(f"Erro ao aceitar conexão: {e}")
        # O servidor vai continuar tentando aceitar novas conexões

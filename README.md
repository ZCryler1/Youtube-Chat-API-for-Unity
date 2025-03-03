# YTChat - Captura de Mensagens do Chat do YouTube  

Este script captura mensagens de um chat ao vivo do YouTube e envia determinadas mensagens para um cliente via conexão TCP.  

## 📌 Funcionalidades  
- Captura mensagens em tempo real de um chat ao vivo do YouTube.  
- Filtra mensagens que contenham palavras-chave específicas.  
- Envia mensagens filtradas para um cliente TCP (como um jogo no Unity).  

## ⚙️ Como Funciona  
1. O script inicia um servidor TCP na porta `5001`.  
2. Aguarda conexões de um cliente.  
3. Captura mensagens do chat ao vivo do YouTube.  
4. Filtra mensagens que contenham palavras-chave como `TNT`, `FERRO`, `DIAMANTE`, etc.  
5. Envia as mensagens filtradas ao cliente TCP em formato JSON.  

## 🛠️ Requisitos  
- Python 3.x  
- Bibliotecas:  
  ```sh
  pip install chat-downloader
  ```  

## 🚀 Como Usar  
1. **Edite a URL do YouTube** no código para apontar para o chat ao vivo desejado.  
2. **Execute o servidor:**  
   ```sh
   python YTChat.py
   ```  
3. **Conecte um cliente TCP** (como um jogo Unity) à porta `5001` para receber as mensagens filtradas.  

## 📜 Licença  
Este projeto é de código aberto. Sinta-se à vontade para modificar e utilizar conforme necessário!  

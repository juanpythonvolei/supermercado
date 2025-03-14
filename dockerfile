# Use uma imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos de requisitos para o contêiner
COPY requirements.txt requirements.txt

# Instale as dependências
RUN pip install -r requirements.txt

# Copie todos os arquivos do projeto para o contêiner
COPY . .

# Exponha a porta em que o Flask irá rodar (por exemplo, 5000)
EXPOSE 5000

# Defina o comando para rodar a aplicação
CMD ["python", "app.py"]

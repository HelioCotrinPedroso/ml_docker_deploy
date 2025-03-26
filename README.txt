# Instale o Docker Desktop.

# Abra a janela do Docker Desktop e mantenha aberta para inicializar o motor de execução Docker.

# Abra o terminal ou prompt de comando, navegue até a pasta com o Dockerfile e execute o comando abaixo para criar a imagem:

# Construir a imagem Docker
docker build -t img-lab2 .

# Criar o Container e Executar a aplicação na porta 8501:8501
docker run -dit --name container-lab2 -p 8501:8501 img-lab2
# Comandos iniciais

- Apresenta a versão do Docker
    ```sh
    docker -v
    ```

- Apresenta a versão do Docker Compose
    ```sh
    docker compose version
    ```

- Baixa a imagem hello-world do DockerHub e executa o container com essa imagem
    ```sh
    docker run hello-world
    ```

- Baixa a imagem dpage/pgadmin4
    ```sh
    docker pull dpage/pgadmin4
    ```

- Lista as imagens na máquina hospedeira
    ```sh
    docker image ls
    ```

- Executa o container com a imagem do dpage/pgadmin4
    ```sh
    docker run -e PGADMIN_DEFAULT_EMAIL=email@email.com -e PGADMIN_DEFAULT_PASSWORD=1234 -p 8080:80 -d --name pgadmin dpage/pgadmin4
    ```

    >Obs.: Sobre as flags utilizadas:
    >
    >  -e: Configura uma variável de ambiente. Sintaxe: NOME_DA_VARIAVEL=valor
    >
    >  -p: Mapea a porta do container para a máquina hospedeira. Sintaxe: porta_da_máquina_hospedeira:porta_do_container
    >
    >  -d: Desanexa a execução do container do terminal. O container irá executar em background.
    >
    >  --name: Configura o nome do container

- Lista os containers em execução
    ```sh
    docker ps
    ```

- Lista todos os containers (parados e em execução)
    ```sh
    docker ps -a
    ```

- Mostra o log do container pgadmin
    ```sh
    docker logs pgadmin -f 
    ```

- Para o container pgadmin
    ```sh
    docker stop pgadmin
    ```

- Remove o container pgadmin, se ele estiver parado 
    ```sh
    docker container rm pgadmin
    ```

- Remove a imagem dpage/pgadmin4, se ela não estiver sendo utilizada
    ```sh
    docker image rm dpage/pgadmin4
    ```

- Remove todos os containers parados 
    ```sh
    docker container prune
    ```

- Remove todas as imagens sem tag ( < none > )
    ```sh
    docker image prune
    ```
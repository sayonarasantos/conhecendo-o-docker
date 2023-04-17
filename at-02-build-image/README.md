# Comandos

- Constroi a imagem com o nome **app1**
    ```sh
    docker build . -t app1
    ```

- Cria e sobe um container chamado **test** a partir da imagem **app1**
    ```sh
    docker run --name test app1
    ```
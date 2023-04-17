# Comandos

- Sobe todos os serviços do compose. 
    ```sh
    docker compose up -d
    ```

    > A flag `-d` desanexa a execução dos containers do terminal.

- Para e remove todos os serviços
    ```sh
    docker compose down
    ```

- Para e remove todos os serviços, além de remover os volumes
    ```sh
    docker compose down -v
    ```
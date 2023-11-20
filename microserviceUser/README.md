# Microserviço de Usuários (microserviceUser)

## Configuração do Ambiente

1. Instale o Docker e o Docker Compose.

2. Execute o seguinte comando para construir e iniciar os contêineres:

    ```bash
    docker-compose up --build
    ```

3. Acesse o Swagger em [http://localhost:8000/swagger/](http://localhost:8000/swagger/) para interagir com a API.

## Endpoints

- **Listar todos os usuários:**

    `GET /api/users/`

- **Visualizar um usuário específico:**

    `GET /api/users/{id}/`

- **Inserir um novo usuário:**

    `POST /api/users/`

    ```json
    {
        "name": "Nome do Usuário",
        "email": "usuario@email.com"
        
    }
    ```

- **Atualizar um usuário:**

    `PUT /api/users/{id}/`

    ```json
    {
        "name": "Novo Nome do Usuário"
        
    }
    ```

- **Excluir um usuário:**

    `DELETE /api/users/{id}/`

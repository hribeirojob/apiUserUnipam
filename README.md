# Microserviço de Usuários (microserviceUser)

## Configuração do Ambiente

1. Instale o Docker e o Docker Compose.

2. Execute o seguinte comando para construir e iniciar os contêineres:

    ```bash
    PASS_ADMIN='suasenha' docker-compose up --build -d
    ```
    O PASS_ADMIN se refere a senha do usuario admin que sera criado para gerar seu token.

    Todas as rotas e obrigatorio utilizar um token exceto a `/swagger`, ` /admin` e `/api-token-auth`

    Apos gerar seu token utilize ele no botao `Autorize` do lado direto no inicio da tela ou pelo cadeado logo a frente do request que deseja utilizar.


3. Acesse o Swagger em [http://localhost:8000/swagger/](http://localhost:8000/swagger/) para interagir com a API.

## Endpoints

- **Input usuário e senha para gerar seu token:**

    `POST ​/api-token-auth​/`

    request
    ```json
    {
        "username": "seuUser",
        "password": "password"
    }
    ```
     response
    ```json
    {
        "token": "seutoken"
    }
    ```

- **Listar todos os usuários:**

    `GET /users/`

- **Visualizar um usuário específico:**

    `GET /users/{id}/`

- **Inserir um novo usuário:**

    `POST /users/`

    ```json
    {
        "name": "Nome do Usuário",
        "email": "usuario@email.com"
        
    }
    ```

- **Atualizar um usuário:**

    `PUT /users/{id}/`

    ```json
    {
        "name": "Novo Nome do Usuário"
        
    }
    ```

- **Excluir um usuário:**

    `DELETE /users/{id}/`



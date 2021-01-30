## Como rodar este projeto
É necessário ter instalado o Docker localmente
https://docs.docker.com/engine/install/ubuntu/

## Comandos
- Iniciar containers:
`docker-componse up`

- Finalizar containers:
`docker-componse down`

- Listar Serviços ativos:
`docker-compose ps`

- Select no banco:
`docker-compose exec db psql -U postgres -d email_sender -c 'select * from emails'`

- Iniciar escalando containers de Worker:
`docker-compose up --scale worker=3`

- Logs dos Workers:
`docker-compose logs -f -t worker`

## Server
http://localhost:80

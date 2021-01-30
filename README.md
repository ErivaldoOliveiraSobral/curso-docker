## Comandos
- Iniciar containers
`docker-componse up`

- Finalizar containers
`docker-componse down`

- Listar Serviços ativos
`docker-compose ps`

- Select no banco
`docker-compose exec db psql -U postgres -d email_sender -c 'select * from emails'`

- Iniciar escalando containers de Worker
`docker-compose up --scale worker=3`

- Los dos Workers
`docker-compose logs -f -t worker`
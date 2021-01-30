import os
import psycopg2
import redis
import json
from bottle import Bottle, request

class Sender(Bottle):
    def __init__(self):
        super().__init__()
        self.route('/', method='POST', callback=self.send)

        redis_host = os.getenv('REDIS_HOST', 'queue')
        self.fila = redis.StrictRedis(host=redis_host, port=6379, db=0)


        db_name = os.getenv('DB_NAME', 'email_sender')
        db_user = os.getenv('DB_USER', 'postgres')
        db_host = os.getenv('DB_HOST', 'db')
        DSN = f'dbname={db_name} user={db_user} host={db_host}'
        self.connection = psycopg2.connect(DSN)


    def register_message(self, assunto, mensagem):
        SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'
        cursor = self.connection.cursor()

        inserted_values = (assunto, mensagem)
        cursor.execute(SQL, inserted_values)

        self.connection.commit()
        count = cursor.rowcount
        print (count, "Successfully inserted")

        cursor.close()

        msg = {'assunto': assunto, 'mensagem': mensagem}
        self.fila.rpush('sender', json.dumps(msg))
        
    def send(self):
        assunto = request.forms.get('assunto')
        mensagem = request.forms.get('mensagem')

        self.register_message(assunto, mensagem)

        return 'Mensagem enfileirada com sucesso! Assunto: {} Mensagem: {}'.format(
            assunto, mensagem
        )

# @route('/', method='GET')
# def send():
#     return 'Servidor de Aplicação'

if __name__ == '__main__':
    sender = Sender()
    sender.run(host='0.0.0.0', port=8080, debug=True)
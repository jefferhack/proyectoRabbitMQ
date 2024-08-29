import pika

# Conexión al servidor de RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Conectar a la cola 'tareas'
channel.queue_declare(queue='tareas')

# Definir la función que procesará los mensajes
def callback(ch, method, properties, body):
    print(f"[x] Recibido: {body.decode()}")

# Indicarle a RabbitMQ que escuche en la cola 'tareas'
channel.basic_consume(queue='tareas', on_message_callback=callback, auto_ack=True)

print(' [*] Esperando mensajes. Presiona CTRL+C para salir')

# Iniciar la escucha
channel.start_consuming()

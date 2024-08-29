import pika

# Conexión al servidor de RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Crear o conectar a la cola 'tareas'
channel.queue_declare(queue='tareas')

print(" [*] Escribe una nueva tarea y presiona Enter para enviarla.")
print(" [*] Escribe 'salir' para terminar el programa.\n")

while True:
    mensaje = input("Nueva tarea: ")

    if mensaje.lower() == 'salir':
        break

    # Publicar el mensaje en la cola 'tareas'
    channel.basic_publish(exchange='', routing_key='tareas', body=mensaje)
    print(f"[x] Enviado: {mensaje}")

# Cerrar la conexión
connection.close()
print(" [x] Publicador cerrado.")

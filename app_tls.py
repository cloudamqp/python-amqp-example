import pika, os

# Access the CLOUDAMQP_URL environment variable and parse it
# (fallback to localhost)
# In a use case where you want to secure the communication between RabbitMQ and
# your app using TLS support.
# As per the documentation here: https://www.cloudamqp.com/docs/amqp.html
# 1. You have to change the port to 5671
# 2. You have to change the protocol string to `amqps://`
url = os.environ.get('CLOUDAMQP_URL', 'amqps://guest:guest@localhost:5671/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start a channel
channel.queue_declare(queue='hello')  # Declare a queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello CloudAMQP!')

print(" [x] Sent 'Hello CloudAMQP!'")


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()

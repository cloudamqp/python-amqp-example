import pika, os, logging
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
# send a message
channel.basic_publish(exchange='', routing_key='hello', body='Hello CloudAMQP!')
print " [x] Sent 'Hello World!'"

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  print " [x] Received %r" % (body)

# set up subscription on the queue
channel.basic_consume(callback,
    queue='hello',
    no_ack=True)

channel.start_consuming() # start consuming (blocks)

connection.close()


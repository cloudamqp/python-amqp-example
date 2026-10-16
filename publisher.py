import pika

import amqp


def publish(channel, queue, message):
    channel.queue_declare(queue=queue, durable=True)
    channel.confirm_delivery()
    channel.basic_publish(
        exchange="",
        routing_key=queue,
        body=message,
        properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
    )
    print(f" [x] Sent {message!r}")


if __name__ == "__main__":
    with amqp.connect() as connection:
        publish(connection.channel(), "hello", "Hello CloudAMQP!")

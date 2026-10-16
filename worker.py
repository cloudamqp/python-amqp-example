import amqp


def consume(channel, queue, handler):
    channel.queue_declare(queue=queue, durable=True)
    channel.basic_qos(prefetch_count=10)

    def on_message(ch, method, properties, body):
        handler(body.decode())
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=queue, on_message_callback=on_message)


if __name__ == "__main__":
    with amqp.connect() as connection:
        channel = connection.channel()
        consume(channel, "hello", lambda message: print(f" [x] Received {message!r}"))
        print(" [*] Waiting for messages. To exit press CTRL+C")
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            pass

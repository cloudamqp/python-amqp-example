import uuid

import amqp
import publisher
import worker


def test_worker_receives_published_message():
    queue = f"roundtrip-{uuid.uuid4()}"
    received = []

    with amqp.connect() as connection:
        consumer_channel = connection.channel()
        worker.consume(consumer_channel, queue, received.append)

        publisher.publish(connection.channel(), queue, "Hello CloudAMQP!")

        connection.process_data_events(time_limit=5)
        consumer_channel.queue_delete(queue)

    assert received == ["Hello CloudAMQP!"]

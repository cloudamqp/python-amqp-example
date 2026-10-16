# Use CloudAMQP from Python

A minimal example of publishing and consuming messages with
[Pika](https://github.com/pika/pika), against [CloudAMQP](https://www.cloudamqp.com)
or any AMQP 0-9-1 broker such as [LavinMQ](https://lavinmq.com) or RabbitMQ.

- [`publisher.py`](publisher.py) publishes a persistent message with publisher confirms.
- [`worker.py`](worker.py) consumes with manual acknowledgements and a prefetch of 10.
- [`amqp.py`](amqp.py) connects using the `CLOUDAMQP_URL` environment variable.

## Usage

Tool versions are in `mise.toml`; with [mise](https://mise.jdx.dev) a virtualenv
is created in `.venv` automatically. Otherwise use Python 3 and a virtualenv.

```sh
pip install -r requirements.txt
export CLOUDAMQP_URL="amqps://user:password@host/vhost"
python worker.py      # in one terminal
python publisher.py   # in another
```

Without `CLOUDAMQP_URL` it connects to `amqp://guest:guest@localhost`.

## Tests

`pytest` publishes and consumes a message through a real broker on localhost.
CI runs it against LavinMQ.

```sh
pip install -r requirements-dev.txt
pytest
```

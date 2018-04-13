from kiel import clients
from tornado import gen


producer = clients.Producer(
    ["kafka01", "kafka02"],
    key_maker=None,
    partitioner=None,
    serializer=None,
    compression=None,
    batch_size=1,
    required_acks=1,
    ack_timeout=500,
)


@gen.coroutine
def run():
    yield producer.connect()
    yield producer.produce("example.topic", {"my": "message"})



if __name__ == '__main__':
    run()

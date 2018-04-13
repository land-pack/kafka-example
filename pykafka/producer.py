from kafka import KafkaProducer
import msgpack



# producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
# Asynchronous by default
# future = producer.send('my-topic', b'raw_bytes')

#producer = KafkaProducer(value_serializer=msgpack.dumps)
#future = producer.send('my-topic', {'name': 'frank'})

producer = KafkaProducer()
future = producer.send('my-topic', key='name', value='frank')

try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    print('xx')

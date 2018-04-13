from kafka import KafkaProducer
import msgpack
import json

data = {"create_time": "2018-03-01 09:43:29", "device_id": "0000002033_0005", "estate_id": "0000002033", "function_name": "mult", "is_alarm": "false", "is_count_people": 0, "people_count": "1", "pic_snap_list": [{"create_time": "09:43:29", "pic": "078f2b674e335ee20e89b405765dda82_1519868609"}]}


# producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
# Asynchronous by default
# future = producer.send('my-topic', b'raw_bytes')

#producer = KafkaProducer(value_serializer=msgpack.dumps)
#future = producer.send('my-topic', {'name': 'frank'})

producer = KafkaProducer()
future = producer.send('msg_notify', 'xxx')
future = producer.send('estate_notify', 'xestate_notify')


future = producer.send('device_upload', json.dumps(data))



try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    print('xx')

from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('my-topic',
                        group_id='my-group',
                        bootstrap_servers=['localhost:9092'])

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("{}:{}:{}: key={} value={}".format(
        message.topic, message.partition,
        message.offset, message.key, message.value
    ))

##KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)
##
### consume json messages
##KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))
##
### consume msgpack
##KafkaConsumer(value_deserializer=msgpack.unpackb)


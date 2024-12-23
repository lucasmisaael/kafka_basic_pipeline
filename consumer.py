from kafka import KafkaConsumer
import json

consumer_conf = {
    'bootstrap_servers': ['localhost:9092'],
    'group_id': 'my_group',
    'auto_offset_reset': 'latest',
    'value_deserializer': lambda v: json.loads(v.decode('utf-8'))

}

consumer=KafkaConsumer('test-topic', **consumer_conf)

for message in consumer:
    print(f"Received message: {message.value}")

consumer.close()

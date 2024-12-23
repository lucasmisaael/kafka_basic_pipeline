from kafka import KafkaProducer
import json
import time

producer_conf={
    'bootstrap_servers': ['localhost:9092'],
    'value_serializer': lambda v: json.dumps(v).encode('utf-8')
}

producer=KafkaProducer(**producer_conf)

topic_name='test-topic'

for i in range(100):
    message={'this is message # :':i}

    producer.send(topic_name,value=message)
    print(f'message sent:{message}')
    time.sleep(1)

"""
    kafka producer
"""
import time, json, uuid, random
import arrow
from faker import Faker
from confluent_kafka import Producer, KafkaError

SETTINGS = {
    'bootstrap.servers': 'kafka-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092',
    'group.id': 'kafka-lena-test-producer'
}

PRODUCER = Producer(SETTINGS)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}: {1}".format(msg.value(), err.str()))
    else:
        print("Message produced: {}".format(msg.value().decode("utf-8")))

FAKER = Faker()

try:
    while True:
        value = {}
        key = uuid.uuid4()
        name = FAKER.first_name()
        age = random.randint(18, 100)
        value["name"] = name
        value["age"] = age
        value["time"] = str(arrow.utcnow())
        PRODUCER.produce('lena-test', key = name, value = json.dumps(value), callback = acked)
        PRODUCER.poll(0.5)
        time.sleep(5)
except KeyboardInterrupt:
    pass

PRODUCER.flush(30)
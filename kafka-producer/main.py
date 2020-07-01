"""
    kafka producer
"""
import time, json, uuid, random
import arrow
from faker import Faker
from confluent_kafka import Producer, KafkaError
from geopy.geocoders import Nominatim
import barnum

CATEGORIES = ['Accessoires', 'Bademode', 'Blazer', 'Blusen', 'Fleece', 'Freizeitmode', 
                'Hosen', 'Jacken', 'Jeans', 'Kleider', 'Mäntel', 'Pullover & Strick', 
                'Röcke', 'Schmuck', 'Schürzen & Kasacks', 'Shirtjacken', 'Shirts', 'Tops',
                'Tuniken', 'Westen', 'Ballerinas', 'Gesundheitsschuhe', 'Halbschuhe', 'Hausschuhe',
                'Pantoletten', 'Pumps', 'Sandaletten', 'Stiefel', 'Stiefeletten']

SETTINGS = {
    'bootstrap.servers': 'kafka-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092',
    'group.id': 'kafka-druid-test-producer'
}

PRODUCER = Producer(SETTINGS)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}: {1}".format(msg.value(), err.str()))
    else:
        # print("Message produced: {}".format(msg.value().decode("utf-8")))
        pass

FAKER = Faker()

try:
    while True:
        key = uuid.uuid4()
        profile = FAKER.profile()
        profile.pop('ssn')
        profile.pop('blood_group')
        profile.pop('website')
        profile.pop('username')
        profile.pop('residence')
        profile.pop('current_location')
        geolocator = Nominatim(user_agent="kafka-producer")
        address = barnum.create_city_state_zip()
        location = geolocator.geocode('{} United States'.format(address[1]))
        profile['longitude'] = location.longitude
        profile['latitude'] = location.latitude
        profile['birthdate'] = str(profile['birthdate'])
        profile['article'] = random.choice(CATEGORIES)
        profile['address'] = ' '.join(address)
        profile['time'] = str(arrow.utcnow())
        PRODUCER.produce('druid-test', key = profile['time'], value = json.dumps(profile), callback = acked)
        PRODUCER.poll(0.5)
        time.sleep(5)
except KeyboardInterrupt:
    pass

PRODUCER.flush(30)
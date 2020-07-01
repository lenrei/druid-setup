from faker import Faker
import random
import json
from geopy.geocoders import Nominatim
import barnum

CATEGORIES = ['Accessoires', 'Bademode', 'Blazer', 'Blusen', 'Fleece', 'Freizeitmode', 
                'Hosen', 'Jacken', 'Jeans', 'Kleider', 'Mäntel', 'Pullover & Strick', 
                'Röcke', 'Schmuck', 'Schürzen & Kasacks', 'Shirtjacken', 'Shirts', 'Tops',
                'Tuniken', 'Westen', 'Ballerinas', 'Gesundheitsschuhe', 'Halbschuhe', 'Hausschuhe',
                'Pantoletten', 'Pumps', 'Sandaletten', 'Stiefel', 'Stiefeletten']

PROFILE = Faker().profile()

PROFILE.pop('ssn')
PROFILE.pop('blood_group')
PROFILE.pop('website')
PROFILE.pop('username')
PROFILE.pop('residence')
PROFILE.pop('current_location')
geolocator = Nominatim(user_agent="kafka-producer")
address = barnum.create_city_state_zip()
location = geolocator.geocode('{} United States'.format(address[1]))
PROFILE['longitude'] = location.longitude
PROFILE['latitude'] = location.latitude
PROFILE['birthdate'] = str(PROFILE['birthdate'])
PROFILE['article'] = random.choice(CATEGORIES)
PROFILE['address'] = ' '.join(address) 
print(json.dumps(PROFILE))

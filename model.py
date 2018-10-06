from math import radians, cos, sin, asin, sqrt


class Incident:

    def __init__(self, identifier, name, category, coordinate, description, date, time, advisory):
        self.id = identifier
        self.name = name
        self.category = category
        self.coordinate = coordinate
        self.description = description
        self.date = date
        self.time = time
        self.advisory = advisory


class Contact:
    AUTHORITY_POLICE = 0

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    @staticmethod
    def retrieve_authority_contact(authority):
        if authority == Contact.AUTHORITY_POLICE:
            return Contact('Police', '+6591515341')
        else:
            raise ValueError("Authority is undefined")


class Person(Contact):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    def __init__(self, name, phone, gender, address):
        super().__init__(name, phone)
        self.gender = gender
        self.address = address


class Address:

    def __init__(self, street_name, unit_number, postal_code, coordinates):
        self.street_name = street_name
        self.unit_number = unit_number
        self.postal_code = postal_code
        self.coordinates = coordinates


class GeoCoordinate:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def calculate_distance(self, destination):
        lon1, lat1, lon2, lat2 = map(radians, [self.longitude, self.latitude,
                                               destination.longitude, destination.latitude])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))

        return c * 6371


def retrieve_nearby_residents(incident, max_distance):
    person_list = [
        Person("Tan Ying Hao", '+6591515341', Person.GENDER_MALE,
               Address('Blk 540 Jelepang Road', '20-36', '670540',
                       GeoCoordinate(1.384860, 103.766550))),
        Person("Lim Xuan Yin", '+6590290589', Person.GENDER_MALE,
               Address('Blk 487 Tampines Street Avenue 4', '03-99', '520487',
                       GeoCoordinate(1.360320, 103.944397)))
    ]

    nearby = []
    for person in person_list:
        if person.address.coordinates.calculate_distance(incident.coordinate) <= max_distance:
            nearby.append(person)

    return nearby

import sys


class Car(object):
    def __init__(self, name='General', model='GM', car_type=None):
        self.model = model
        self.name = name
        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        if len(sys.argv) >= 3:
            self.car_type = 'trailer'
        else:
            self.car_type = 'saloon'
        if self.car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
        self.speed = 0

    def is_saloon(self):
        return self.car_type

    def drive(self, velocity):
        if self.car_type == 'trailer':
            self.speed = 11 * velocity
            return self

        elif self.is_saloon():
            self.speed = 10 ** velocity
            return self

class Vehicle(object):

    def __init__(self, engine_type, **kwargs):
        self.engine_type = engine_type
        for k, v in kwargs.items():
            setattr(self, k, v) 
            # self[k] = v


    def set_color(self, color):
        self.color = color

    def set_speed(self, speed):
        self.speed = speed

class Car(Vehicle):

    def __init__(self, engine_type, car_category, **kwargs):
        super(Car, self).__init__(engine_type, **kwargs)
        self.car_category = car_category
        self.doors = 5
        self.wheels = 4

my_car = Car('VTI-120', 'saloon',
            engine_cc=1500,
            color='red',
            max_speed=120)

print my_car.max_speed



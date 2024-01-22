class car: 
    def __init__ (self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
        
    def car_info(self):
        print(f'{self.model} {self.make} {self.year}')
        
my_car = car('audi', 'bmw', 2020)

print(my_car.make)
my_car.car_info()
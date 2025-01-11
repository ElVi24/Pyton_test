class Car:
    def __init__(self, model, year, engine_volume, price, car_mileage): #создание класса Car
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.price = price
        self.car_mileage = car_mileage
        self.weels = 4 # по умолчанию

    def description(self): # возвращает информацию по объекту
        description = (f"Модель: {self.model}\nГод выпуска: {self.year}\nОбъем двигателя: {self.engine_volume} л\n"
                    f"Цена: {self.price} руб\nПробег: {self.car_mileage} км")
        return description
# создание экземпляра класса Car
car = Car('Kia Sportage','2024','2','3000000','1' )
print ('Информация об автомобиле')
print (car.description())

#создание наследника класса Car - Truck (грузовик)
class Truck(Car):
    def __init__(self, model, year, engine_volume, price, car_mileage):
        super().__init__(model, year, engine_volume, price, car_mileage)
        self.weels = 8 # по умолчанию во всем классе
    def description(self): # возвращает информацию по объекту
        description = (f"Модель: {self.model}\nГод выпуска: {self.year}\nОбъем двигателя: {self.engine_volume} л\n"
                    f"Цена: {self.price} руб\nПробег: {self.car_mileage} км\nКоличество колес:{self.weels}")
        return description
# создание экземпляра наследника Truck
truck = Truck('КАМАЗ 6560-23960-53','2024','400','11500000', '12', )
print ('\nИнформация о грузовике')
print (truck.description())






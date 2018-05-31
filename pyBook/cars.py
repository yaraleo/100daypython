cars = ['bmw', 'audi', 'toyota', 'subaru']

print(cars)
for car in cars:
    if car != 'audi':
        print(car.title())
    else:
        print(car.upper())

print('bmw' in cars)
print("ausddi" in cars)

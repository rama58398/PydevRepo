def car_info(name, model, **car):
    car['Make'] = name
    car['Model'] = model
    return car

car_details=car_info('tesla','model y',color='blue',type='long range ')
print(car_details)
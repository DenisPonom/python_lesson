# Пользователь вводит время в секундах. Переведите время в часы, минуты,
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

enter_time = int(input('Enter time in seconds '))
hours = enter_time // 3600
rest_time = enter_time % 3600
minutes = rest_time // 60
secs = rest_time % 60
print(f'{enter_time} sec is {hours} hours {minutes} minutes {secs} seconds')

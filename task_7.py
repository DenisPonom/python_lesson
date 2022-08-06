# Спортсмен занимается ежедневными пробежками. В первый день его результат
# составил a километров. Каждый день спортсмен увеличивал результат на 10%
# относительно предыдущего. Требуется определить номер дня, на который
# результат спортсмена составит не менее b километров. Программа должна
# принимать значения параметров a и b и выводить одно натуральное
# число — номер дня.


start = float(input('Enter start result '))
finish = float(
    input('Enter finish result '))
day = 1
while start < finish:
    start = start + start / 10
    day += 1
else:
    print('Already finished')
print(f'Result achieved in {day} days')

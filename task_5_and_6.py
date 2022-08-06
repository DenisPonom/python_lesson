# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это
# отношение прибыли к выручке. Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчёте на одного сотрудника.

revenue = int(input('Enter revenue '))
costs = int(input('Enter costs '))
if revenue > costs:
    profit = revenue - costs
    rent = profit / revenue
    print(f'Profit is {profit}')
    workers = int(input('Enter number of workers '))
    prof_per_worker = profit / workers
    print(f'Profit per worker is {prof_per_worker}')
elif revenue == costs:
    print('Your revenue equals costs')
else:
    print('Your company is in bad situation')

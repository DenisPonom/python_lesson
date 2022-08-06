# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

input_number = input('Enter any number ')
number_1 = int(input_number + input_number)
number_2 = int(input_number + input_number + input_number)
print(int(input_number) + number_1 + number_2)

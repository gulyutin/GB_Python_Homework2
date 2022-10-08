# Задайте список из n чисел последовательности (1+\frac 1 n)^n и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


def input_int(msg):
    while True:
        try:
            result = int(input(msg))
        except ValueError:
            print('Неверные данные')
        else:
            return result

def generate_list(n):
    result = []
    for i in range(1, n+1):
        result.append(round(1 + 1/i) ** i)
    return result

n = input_int("Введите целое число: ")
number_list = generate_list(n)

print(f"Для n = {n}: {number_list}. Сумма = {sum(number_list)}")
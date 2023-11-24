
# Задача 1: Найти количество положительных чисел в исходном наборе.
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))

positive_count = 0

if first_number > 0:
    positive_count += 1
if second_number > 0:
    positive_count += 1
if third_number > 0:
    positive_count += 1

print(f"Количество положительных чисел: {positive_count}")

# Задача 2: Вывести большее из двух чисел.
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

if first_number > second_number:
    print(f"Большее число: {first_number}")
else:
    print(f"Большее число: {second_number}")

# Задача 3: Вывести сначала большее, а затем меньшее из двух чисел.
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

if first_number > second_number:
    print(f"Большее число: {first_number}")
    print(f"Меньшее число: {second_number}")
else:
    print(f"Большее число: {second_number}")
    print(f"Меньшее число: {first_number}")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число:"))

# Определение наименьшего числа с использованием операторов if-else
min_number = a  # Пусть первое число будет начальным минимальным

if b < min_number:
    min_number = b

if c < min_number:
    min_number = c

# Вывод результата
print("Наименьшее число:", min_number)

# Ввод данных
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

# Определение номера координатной четверти
if x > 0 and y > 0:
    print("Точка находится в первой координатной четверти.")
elif x < 0 and y > 0:
    print("Точка находится во второй координатной четверти.")
elif x < 0 and y < 0:
    print("Точка находится в третьей координатной четверти.")
elif x > 0 and y < 0:
    print("Точка находится в четвертой координатной четверти.")
else:
    print("Точка лежит на одной из координатных осей.")

K = int(input("Enter the grade (1-5): "))

match K:
    case 1:
        print("Poor")
    case 2:
        print("Unsatisfactory")
    case 3:
        print("Satisfactory")
    case 4:
        print("Good")
    case 5:
        print("Excellent")
    case _:
        print("Error")

month = int(input("Enter the month (1-12): "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 days")
    case 4 | 6 | 9 | 11:
        print("30 days")
    case 2:
        print("28 days")
    case _:
        print("Invalid month")

D = int(input("Enter the day: "))
M = int(input("Enter the month: "))

days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

match (M, D):
    case (1, 1):
        print("Invalid date")
    case (_, 1) if D <= days_in_month[M - 1]:
        print(f"Next date: {D + 1}.{M}")
    case (_, _) if D <= days_in_month[M]:
        print(f"Next date: {D + 1}.{M}")
    case (_, _) if M < 12:
        print(f"Next date: 1.{M + 1}")
    case (_, _):
        print("Invalid date")


C = input("Enter the initial direction (N, W, S, E): ")
N = int(input("Enter the command (-1, 0, 1): "))

directions = {'N': 0, 'W': 1, 'S': 2, 'E': 3}
direction_list = list(directions.keys())

new_direction = (directions[C] + N) % 4

match new_direction:
    case 0:
        print("New direction: North")
    case 1:
        print("New direction: West")
    case 2:
        print("New direction: South")
    case 3:
        print("New direction: East")

number = int(input("Enter a number (100-999): "))

match number:
    case n if 100 <= n <= 999:
        hundreds = n // 100
        tens = (n % 100) // 10
        ones = n % 10

        result = []

        if hundreds > 0:
            result.append(f"{hundreds * 100}")

        if tens > 1:
            result.append(f"{tens * 10}")

        if ones > 0:
            result.append(f"{ones}")

        print(' '.join(result))
    case _:
        print("Invalid number")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

try:
    match operation:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
        case '/' if b != 0:
            result = a / b
        case _:
            raise ValueError("Неверная операция")

    print(f"Результат: {result}")

except ZeroDivisionError:
    print("Ошибка: Деление на ноль")
except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")

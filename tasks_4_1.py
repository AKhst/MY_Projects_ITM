
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


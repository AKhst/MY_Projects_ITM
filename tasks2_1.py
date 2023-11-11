# Задача 1
def meters_from_centimeters(cm):
    return cm // 100

# Задача 2
def tons_from_kilograms(kg):
    return kg // 1000

# Задача 3
def kilobytes_from_bytes(bytes):
    return bytes // 1024

# Задача 4
def segments_on_segment(A, B):
    return A // B

# Задача 5
def remaining_length(A, B):
    return A % B

# Задача 6
def left_and_right_digits(number):
    tens = number // 10
    ones = number % 10
    return tens, ones

# Задача 7
def sum_and_product_of_digits(number):
    tens = number // 10
    ones = number % 10
    return tens + ones, tens * ones

# Задача 8
def reversed_number(number):
    tens = number // 10
    ones = number % 10
    return ones * 10 + tens

# Задача 9
def hundreds_digit(number):
    return number // 100

# Задача 10
def last_and_middle_digits(number):
    ones = number % 10
    tens = (number // 10) % 10
    return ones, tens

if __name__ == "__main__":
    cm = int(input("Введите расстояние в сантиметрах: "))
    kg = int(input("Введите массу в килограммах: "))
    bytes = int(input("Введите размер файла в байтах: "))
    A = int(input("Введите длину отрезка A: "))
    B = int(input("Введите длину отрезка B: "))
    two_digit_number = int(input("Введите двузначное число: "))
    three_digit_number = int(input("Введите трехзначное число: "))

    # Вывод результатов
    print("Задача 1 - Количество метров в сантиметрах:", meters_from_centimeters(cm))
    print("Задача 2 - Количество тонн в килограммах:", tons_from_kilograms(kg))
    print("Задача 3 - Количество килобайтов в байтах:", kilobytes_from_bytes(bytes))
    print("Задача 4 - Количество отрезков B на отрезке A:", segments_on_segment(A, B))
    print("Задача 5 - Длина незанятой части отрезка A:", remaining_length(A, B))
    tens, ones = left_and_right_digits(two_digit_number)
    print("Задача 6 - Десятки и единицы в двузначном числе:", tens, ones)
    sum_digits, product_digits = sum_and_product_of_digits(two_digit_number)
    print("Задача 7 - Сумма и произведение цифр в двузначном числе:", sum_digits, product_digits)
    reversed = reversed_number(two_digit_number)
    print("Задача 8 - Число с переставленными цифрами:", reversed)
    print("Задача 9 - Первая цифра в трехзначном числе (сотни):", hundreds_digit(three_digit_number))
    ones, tens = last_and_middle_digits(three_digit_number)
    print("Задача 10 - Единицы и десятки в трехзначном числе:", ones, tens)
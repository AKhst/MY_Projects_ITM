import math


# Задача 1: Нахождение периметра квадрата
def square_perimeter(a):
    return 4 * a


# Задача 2: Нахождение площади квадрата
def square_area(a):
    return a ** 2


# Задача 3: Свойства прямоугольника
def rectangle_properties(a, b):
    area = a * b
    perimeter = 2 * (a + b)
    return area, perimeter


# Задача 4: Длина окружности
def circle_length(d):
    return math.pi * d


# Задача 5: Объем и площадь поверхности куба
def cube_volume_and_surface_area(a):
    volume = a ** 3
    surface_area = 6 * a ** 2
    return volume, surface_area


# Задача 6: Объем и площадь поверхности параллелепипеда
def cuboid_volume_and_surface_area(a, b, c):
    volume = a * b * c
    surface_area = 2 * (a * b + b * c + a * c)
    return volume, surface_area


# Задача 7: Свойства круга
def circle_properties(R):
    circumference = 2 * math.pi * R
    area = math.pi * R ** 2
    return circumference, area


# Задача 8: Среднее арифметическое двух чисел
def average_of_two_numbers(a, b):
    return (a + b) / 2


# Задача 9: Среднее геометрическое двух чисел
def geometric_mean(a, b):
    return math.sqrt(a * b)


# Задача 10: Операции над квадратами двух чисел
def operations_on_two_numbers(a, b):
    sum_of_squares = a ** 2 + b ** 2
    difference_of_squares = a ** 2 - b ** 2
    product_of_squares = a ** 2 * b ** 2
    quotient_of_squares = (a ** 2) / (b ** 2) if b != 0 else "Деление на ноль!"
    return sum_of_squares, difference_of_squares, product_of_squares, quotient_of_squares


if __name__ == "__main__":
    a, b, c, d, R = 4, 4, 4, 4, 4
    print("Задача 1 - Периметр квадрата:", square_perimeter(a))
    print("Задача 2 - Площадь квадрата:", square_area(a))
    print("Задача 3 - Свойства прямоугольника:", rectangle_properties(a, b))
    print("Задача 4 - Длина окружности:", circle_length(d))
    print("Задача 5 - Объем и площадь поверхности куба:", cube_volume_and_surface_area(a))
    print("Задача 6 - Объем и площадь поверхности параллелепипеда:", cuboid_volume_and_surface_area(a, b, c))
    print("Задача 7 - Свойства круга:", circle_properties(R))
    print("Задача 8 - Среднее арифметическое двух чисел:", average_of_two_numbers(a, b))
    print("Задача 9 - Среднее геометрическое двух чисел:", geometric_mean(a, b))
    print("Задача 10 - Операции над квадратами двух чисел:", operations_on_two_numbers(a, b))

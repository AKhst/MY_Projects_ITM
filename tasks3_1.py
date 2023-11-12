# Задача 1
def is_positive(A):
    return A > 0

# Задача 2
def is_odd(A):
    return A % 2 != 0

# Задача 3
def is_even(A):
    return A % 2 == 0

# Задача 4
def inequalities(A, B):
    return A > 2 and B <= 3

# Задача 5
def compound_inequalities(A, B):
    return A >= 0 or B < -2

# Задача 6
def double_inequalities(A, B, C):
    return A < B and B < C

# Задача 7
def between_numbers(A, B, C):
    return A < B < C or C < B < A

# Задача 8
def both_odd(A, B):
    return A % 2 != 0 and B % 2 != 0

# Задача 9
def at_least_one_odd(A, B):
    return A % 2 != 0 or B % 2 != 0

# Задача 10
def exactly_one_odd(A, B):
    return (A % 2 != 0) != (B % 2 != 0)

if __name__ == "__main__":
    A = int(input("Введите целое число A: "))
    B = int(input("Введите целое число B: "))
    C = int(input("Введите целое число C: "))

    print("Задача 1 - Число A является положительным:", is_positive(A))
    print("Задача 2 - Число A является нечетным:", is_odd(A))
    print("Задача 3 - Число A является четным:", is_even(A))
    print("Задача 4 - Неравенства A > 2 и B ≤ 3:", inequalities(A, B))
    print("Задача 5 - Неравенства A ≥ 0 или B < −2:", compound_inequalities(A, B))
    print("Задача 6 - Двойное неравенство A < B < C:", double_inequalities(A, B, C))
    print("Задача 7 - Число B между A и C:", between_numbers(A, B, C))
    print("Задача 8 - Оба числа A и B нечетные:", both_odd(A, B))
    print("Задача 9 - Хотя бы одно из чисел A и B нечетное:", at_least_one_odd(A, B))
    print("Задача 10 - Ровно одно из чисел A и B нечетное:", exactly_one_odd(A, B))
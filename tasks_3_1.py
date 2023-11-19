def calculate_average():
    try:
        n = int(input("Введите число (или 0 для завершения): "))
        sum_numbers = n
        count = 0

        while n != 0:
            n = int(input("Введите число (или 0 для завершения): "))
            sum_numbers += n
            count += 1

        if count > 0:
            average = sum_numbers / count
            print(f"Среднее значение введенных чисел: {average}")
        else:
            print("Вы не ввели ни одного числа (кроме 0).")

    except ValueError:
        print("Ошибка ввода. Введите корректное число.")
    except ZeroDivisionError:
        print("Программа завершена. Вы ввели 0 сразу после начала выполнения программы.")

def print_numbers(n: int):
    print("Выполнение задачи 2:")
    for i in range(n + 1):
        print(i)

def multiplication_table():
    print("\nВыполнение задачи 3:")
    for i in range(10):
        for j in range(1, 10):
            print(f"{i}*{j} = {i * j}")

def iterate_list():
    print("\nВыполнение задачи 4:")
    my_list = [1, 2, 3, 4, 5]

    print("Итерация по списку:")
    for item in my_list:
        print(item)

def iterate_dict():
    print("\nВыполнение задачи 5:")
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    print("Итерация по словарю:")
    for key, value in my_dict.items():
        print(f"Ключ: {key}, Значение: {value}")

if __name__ == '__main__':
    print("Выполнение задачи 1:")
    calculate_average()

    n = 100
    print_numbers(n)

    multiplication_table()
    iterate_list()
    iterate_dict()

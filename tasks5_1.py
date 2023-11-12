# Задача 1: Создание словаря с данными о человеке
person = {
    "имя": "Иван",
    "возраст": 30,
    "пол": "мужской",
    "рост": 180,
    "вес": 75
}

# Вывод всех данных о человеке по ключам
for key in person:
    print(key + ":", person[key])

person["размер ноги"] = 43
del person["возраст"]

# Алгоритм бинарного поиска
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1
# Алгоритм пузырьковой сортировки
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


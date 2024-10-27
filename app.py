# ### Задача 1. Определение времени
# Напишите функцию `get_time()`, которая принимает
# аргумент со строкой — временем в формате `'hh:mm'`.
# Разбейте аргумент на два целых числа: часы и минуты.
# Верните их в том же порядке, выводом на экран.


def get_time(time_str):
    hours, minutes = map(int, time_str.split(':'))
    print(hours, minutes)


get_time('12:45')


# Задача 2. Обработка музыкальных треков
# 1) Напишите функцию `song_duration()`, которая:
# - принимает аргумент-строку с длительностью трека в формате `mm:ss`;
# - возвращает True, если длительность меньше 210 секунд. Иначе возвращает False.
# Внутри своей функции вызовите `get_min_sec()`, которая позволит извлечь количество минут и секунд из строки.
# 2) Создайте список `tracks` который хранит о продолжительности пяти треков: `2:25, 2:35, 3:45, 2:00, 5:10`.
# 3) Создайте цикл, который проверит длительность треков из списка `tracks`.
# Цикл должен вывести на экран результат работы функции `song_duration()` для каждого элемента списка.

def get_min_sec(duration_str):
    minutes, seconds = map(int, duration_str.split(':'))
    return minutes, seconds


def song_duration(duration_str):
    minutes, seconds = get_min_sec(duration_str)
    total_seconds = minutes * 60 + seconds
    return total_seconds < 210


tracks = ['2:25', '2:35', '3:45', '2:00', '5:10']

for track in tracks:
    print(song_duration(track))


# Задача 3. Свой собственный калькулятор
# 1) Напишите программу на Python для создания калькулятора. Создайте функции для выполнения
# основных арифметических операций: сложение, вычитание, умножение и деление.
# Программа должна предоставлять пользователю возможность вводить два числа и выбирать операцию.
# 2) Создайте функции `addition`, `subtraction`, `multiplication` и `division`
# для выполнения соответствующих арифметических операций.
# 3) Напишите функцию calculator, которая принимает числа и операцию, вызывает
# соответствующую функцию и выводит результат.
# В основной части программы позвольте пользователю вводить два числа
# и выбирать операцию (сложение, вычитание, умножение или деление).
# 4) Обработайте возможные ошибки, такие как деление на ноль или ввод некорректных данных.

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b


def calculator(num1, num2, operation):
    if operation == '+':
        return addition(num1, num2)
    elif operation == '-':
        return subtraction(num1, num2)
    elif operation == '*':
        return multiplication(num1, num2)
    elif operation == '/':
        return division(num1, num2)
    else:
        return "Ошибка: некорректная операция"


try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    operation = input("Выберите операцию (+, -, *, /): ")

    result = calculator(num1, num2, operation)
    print("Результат:", result)

except ValueError:
    print("Ошибка: введите числовое значение.")


# Доп.задача 1: Счетчик частоты элементов в списке.
# Напиши функцию `count_elements(lst)`, которая принимает список чисел
# и возвращает словарь, где ключи — это уникальные элементы списка, а
# значения — количество их появлений в списке.

def count_elements(lst):
    element_count = {}
    for elem in lst:
        if elem in element_count:
            element_count[elem] += 1
        else:
            element_count[elem] = 1
    return element_count


numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(count_elements(numbers))


# Доп. задача 2: Сумма чисел в словаре по ключам.
# Напиши функцию `sum_by_key(data)`, которая принимает список словарей,
# каждый из которых содержит одинаковые ключи с числовыми значениями.
# Функция должна возвращать словарь, где ключи такие же, как в исходных
# словарях, а значения — сумма чисел для каждого ключа из всех словарей.

def sum_by_key(data):
    result = {}
    for d in data:
        for key, value in d.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result


data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "b": 5, "c": 6},
    {"a": 7, "b": 8, "c": 9}
]
print(sum_by_key(data))

### Доп. задача 3: Преобразование строк в заглавные
# 1) Изучите безымянную функцию `lambda x`
# 2) Изучите работу функции `map()` и `upper()`
# 3) Напишите функцию `convert_strings_to_upper(lst)`, которая принимает
# список строк и возвращает новый список, где все строки преобразованы в
# заглавные буквы. Для реализации используйте обычные функции и отдельно безымянную `lambda`.

strings = ["hello", "world", "python"]


def convert_strings_to_upper(lst):
    def to_upper(s):
        return s.upper()

    return list(map(to_upper, lst))


print(convert_strings_to_upper(strings))


def convert_strings_to_upper_lambda(lst):
    return list(map(lambda x: x.upper(), lst))


print(convert_strings_to_upper_lambda(strings))

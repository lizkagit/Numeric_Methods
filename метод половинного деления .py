import random as r

def func(num, arr):
    y = 0
    for i in range(len(arr)):
        y += (num ** i) * arr[i]
    return y

def get_param():
    a = int(input("Введите точку a: "))
    b = int(input("Введите точку b: "))
    E = int(input("Введите точность E: "))
    E = 10 ** (-E)  # Преобразование точности
    numbers = input("Введите числа, разделенные пробелами: ")
    arr = list(map(int, numbers.split()))
    return a, b, E, arr

def start():
    a, b, E, arr = get_param()
    
    while True:
        x_0 = r.randint(a, b)
        x_1 = r.randint(a, b)
        
        if func(x_0, arr) * func(x_1, arr) < 0:
            list_x = [x_0, x_1]
            break  # Нашли подходящие x, выходим из цикла

    iterations = 0
    max_iterations = 100  # Ограничиваем количество итераций для предотвращения бесконечного цикла

    while iterations < max_iterations:
        mid = (list_x[0] + list_x[1]) / 2  # Находим среднюю точку
        
        if func(list_x[0], arr) * func(mid, arr) < 0:
            list_x[1] = mid  # Если знак функции изменился, сужаем промежуток
        else:
            list_x[0] = mid

        # Проверяем, достигли ли нужной точности
        if abs(list_x[0] - list_x[1]) < E:
            return mid  # Возвращаем найденный корень
        
        iterations += 1  # Увеличиваем счетчик итераций

    return (list_x[0] + list_x[1]) / 2  # Возвращаем последнее найденное значение, если не достигнута точность

result = start()
print(f"Приблизительное значение корня: {result}")


 

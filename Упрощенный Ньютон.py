import random as r
import math
def func(num,arr):
    y=0
    for i in range(0,len(arr)):
        y+=(num**i)*arr[i]  

    return y
def deriv(num,arr):
    dy=0
    for i in range(1, len(arr)):
        dy += i * (num ** (i - 1)) * arr[i]  # Производная полинома
    return dy
def get_param():
    a = int(input("Введите точку a: "))
    b = int(input("Введите точку b: ")) 
    E = int(input("Введите точность E: "))
    E = 10 ** (-E)  # Преобразование точности
    numbers = input("Введите числа, разделенные пробелами: ")
    arr = list(map(int, numbers.split()))
    return  a,b,E, arr
def simple_newton_method():
    a,b,E,arr=get_param()
    y=None
    x_0=r.randint(a,b)
    iterations=0
    max_iterations=100
    der=deriv(x_0,arr)
    print('der',der)
    while iterations<max_iterations:
        x_1=x_0-(func(x_0,arr)/der)
        if abs(x_1-x_0)<E:
            y=x_1
            break
        print(x_0,x_1)
        x_0=x_1
        iterations+=1
    return y

result = simple_newton_method()
print(f"Приблизительное значение корня: {result}")
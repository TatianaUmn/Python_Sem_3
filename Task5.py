# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов.

n = int(input('Введите число '))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_negativ(n):
    if n in [0]:
        return 0
    elif n in [-1]:
        return 1
    else:
        return fib_negativ(n + 2) - fib_negativ(n + 1)


list = []
for e in range(1, n+1):
    list.append(fib(e))
ist = []
for e in range(-n, 1):
    ist.append(fib_negativ(e))
result = ist + list
print(result)   


# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.


ist = [int(i) for i in input("Введите числа через пробел: ").split()]
sum = 0
for i in range(0, len(ist)):
    if i % 2 != 0:
        print(ist[i])
        sum += ist[i]
print(sum)
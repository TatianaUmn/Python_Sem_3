# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

list = [float(i) for i in input("Введите числа через пробел: ").split()]
ist = []
for i in list:
    ist.append(i - int(i))
print(max(ist) - min(ist))

# или так, если min и max нужно найти без помощи функций
# min = 1
# max = 0
# for i in list:
#     if (i - int(i)) < min:
#         min = i - int(i)
#     if (i - int(i)) > max:
#         max = i - int(i)
# print(max - min)
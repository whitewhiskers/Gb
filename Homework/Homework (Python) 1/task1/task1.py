# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print("Введите цифру дня недели: ")
number = int(input())
if 0 < number < 6:
    print(f"Ваш {number} день не является выходным")
elif 5 < number < 8:
    print(f"Ваш {number} день является выходным")
else:
    print("Вы ввели некорректное число")
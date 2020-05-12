# Задача 6
a = int(input("Введите пробег спортсмена в первый день:\n"))
b = int(input("Введите ожидаемый результат спортсмена:\n"))
day = 1
actual_result = a
while actual_result < b:
    actual_result = actual_result * 1.1
    day += 1

print(f"Спортсмен достиг ожидаемого результата на {day} день - не менее {b}км в день")



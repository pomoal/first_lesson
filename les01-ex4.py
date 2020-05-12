# Задача 4
import math
a = int(input("Введите целое положительное число:\n"))
digit = a
max_digit = int(math.fmod(int(a),int(10)))
min_digit = max_digit

while (math.fmod(a, 10) >= 0) and (a >= 10):
    a = int(a / 10)
    temp = int(math.fmod(int(a),int(10)))
    if max_digit <= temp:
        max_digit = temp
    elif min_digit >= temp:
        min_digit = temp

print(f"Вы ввели: {digit} \nmax {max_digit} \nmin {min_digit}")

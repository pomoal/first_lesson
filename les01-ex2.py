# Задание №2

import math
sec_quantity = int(input("Введите число секунд:\n"))

hours_count = math.floor(sec_quantity / 3600);
min_count = math.floor(math.fmod(sec_quantity,3600) / 60);
sec_count = sec_quantity - 3600 * hours_count - min_count * 60

if hours_count > 23:
    days_count = math.floor(hours_count / 24);
    print(f' {days_count} days : {hours_count} hours : {min_count} mins : {sec_count} secs ')
else:
    print(f' {hours_count} hours : {min_count} mins : {sec_count} secs')
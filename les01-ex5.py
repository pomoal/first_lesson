# # Задача 5
income = int(input("Введите сумму выручки:\n"))
expenses = int(input("Введите сумму затрат:\n"))
profit = income - expenses
if profit > 0:
    ebitda = (profit / income)
    print(f"Поздравляем! Рентабельность:{ebitda:.2f}.")
    staff_count = int(input("Сколько сотрудников в компании?:"))
    profit_per_person = (ebitda * income) / staff_count
    print(f"Сумма прибыли на 1 сотрудника:{profit_per_person}.")
else: print("Ваша компания убыточна!")

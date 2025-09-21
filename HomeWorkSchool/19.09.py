hours = float(input("Сколько часов - "))

rate = float(input("Скок в час -  "))

if hours > 40:
    regular_pay = 40 * rate
    overtime_pay = (hours - 40) * rate * 1.5
    total_pay = regular_pay + overtime_pay
else:
    total_pay = hours * rate

print("Зарплата до", total_pay)

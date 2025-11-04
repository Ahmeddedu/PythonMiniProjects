import random

N = int(input("Кол числ: "))

suma = 0

for i in range(N):
    num = random.randint(1, 100)
    print(num, " ")
    suma += num

print("Сумма - " , suma)



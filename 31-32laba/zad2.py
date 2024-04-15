print("Введите последовательность чисел которая будет заканчиваться нулем")

list = []

while True:
    a = int(input("Введите число: "))
    if a == 0:
        break
    else:
        list.append(a)

print(list)

print(f'Сумма чисел в последовательности = {sum(list)}')
print(f'Колличество элементов в последовательности = {len(list)}')



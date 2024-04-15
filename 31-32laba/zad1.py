a = int(input('Enter price: '))
quantity = 1

for i in range(10):
    price = a * quantity
    print(f'Цена за {quantity} кг конфет равна: {price}')
    quantity += 1
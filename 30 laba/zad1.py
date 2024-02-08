a = int(input("Введите 1-е число: "))
b = int(input("Введите 2-е число: "))
c = int(input("Введите 3-е число: "))

l = []

if 1 < a < 3:
    l.append(a)
else:
    pass

if 1 < b < 3:
    l.append(b)
else:
    pass

if 1 < c < 3:
    l.append(c)
else:
    pass

print(f"Числа принадлежащие этому интервалу: {l}")
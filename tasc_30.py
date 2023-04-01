a1 = int(input("Введите первый эллемент прогрессии:"))
n = int(input("Введите количество эллементов: "))
d = int(input("Разность эллементов: "))
index_1 = int(input("Введите первый эллемент массива: "))
index_last = int(input("Введите второй эллемент массива: "))
last_el = a1 + (n - 1) * d
print(last_el)
new_list = [el for el in range(a1, last_el + 1, d)]
print(*new_list)

for el in new_list:
    if el >= index_1 and el <= index_last:
        print(el)

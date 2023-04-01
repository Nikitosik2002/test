list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dictionary = {}
for el in list_1:
    if el % 2 == 0:
        dictionary[el] = el*el
print(dictionary)


list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dictionary_1 = list()
for el in list_2:
    if el % 2 == 0:
        dictionary_1.append((el, el**2))
print(dictionary_1)

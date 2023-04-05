arr = [i*j for i in range(1, 7) for j in range(1, 7)]

count = 0
line_count = 6
for el in arr:
    count += 1
    print(el, end=" ")
    if count == line_count:
        print("")
        line_count += 6






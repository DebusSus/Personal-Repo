a = [2, 5, 7, 4 , 99, 20, 11, 3 ]

i = len(a) - 1
while i != 0:
    if a[i] % 2 != 0:
        del a[i]
        
    i -= 1

print(a)
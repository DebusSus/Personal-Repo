a = []
name = 'p'
aux = -1

while name:
    name = input("Input names here: ")
    a.append(name)
    aux += 1

print("Here are the names in the normal order: ")
a.pop(-1)
print(a)

print("Here is the list in desending order: ")
while aux > 0:
    print(a[aux - 1])
    aux -= 1
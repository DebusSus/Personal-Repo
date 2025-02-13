def triangle(n):
    i = 1
    while i != n:
        j = i

        while j != n:
            print(' ', end='')
            j += 1

        aux = i
        while j == n and aux != 0:
            print('*', end='')
            aux -= 1
            

        print()
        i += 1


n = int(input("What is the size of the triangle? "))
triangle(n)
def sum2(n, m):
    return n + m

def sub2(n, m):
   return  n - m


def multi2(n, m):
    return n * m

def divide2(n, m):
    return n / m

def sum3(n, m, x):
    return n + m + x

def sub3(n, m, x):
    return n - m - x


def multi3(n, m, x):
    return n * m * x

def divide3(n, m, x):
    return n / m / x



print("Welcome to the 2 number calculator! ")
print("A calculator that only accepts 2 OR 3 numbers! WOW EXCITING! ")

flag = 'y'

while flag == 'y':

    numbers = int(input("How many numbers would you like to use? (2 OR 3) "))

    if numbers not in [2, 3]:

        while True:

            numbers = input("Please choose between 2 OR 3: ")

            if numbers in [2, 3]:
                break


    a = float(input("Please input the first number: "))
    b = float(input("Please input the second number: "))



    if numbers == 2:

        print("Sum = ", sum2(a, b))
        print("Sub = ", sub2(a, b))
        print("Multi = ", multi2(a, b))
        print("Div = ", divide2(a, b))



    elif numbers == 3:
        c = float(input("Please input the third number: "))
        print("Sum = ", sum3(a, b, c))
        print("Sub = ", sub3(a, b, c))
        print("Multi = ", multi3(a, b, c))
        print("Div = ", divide3(a, b, c))

    flag = input("Would you like to calculate again? (y / n) ")


#for _ in range(numbers):
#    nr = float(input("Please input a number: "))
#    a.append(nr)

#print("The following numbers will be used for calculations: ",a)



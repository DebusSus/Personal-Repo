import math

def is_prime(n):
    i = 3
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    while i <= round(math.sqrt(n)):
        if n % i == 0:
            return False
        else:
            i += 2
    return True

def prime_numbers(nr):
    i = 3
    for i in range(nr):
        if is_prime(i) == True:
            print(i)



n = int(input("Choose a number: "))
prime_numbers(n)
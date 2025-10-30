n = int(input("Enter a number to compute its factorial: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def mainfucn(n):
    factorial((n))
    print(factorial(n))
mainfucn(n)
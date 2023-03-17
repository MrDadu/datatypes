# Factorial Number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input('Enter The Number : '))
factorial(n)

print('The Factorial Of The Number is : ', factorial(n))
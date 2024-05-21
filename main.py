def factorial(n):
    if n <= 1: return 1
    return n * factorial(n)

a = factorial(10)
print(a)
print(a - 10)
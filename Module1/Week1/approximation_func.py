def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


def approx_sin(x, n):
    total = 0
    for i in range(n):
        total += ((-1)**i * x**(2*i + 1)) / factorial(2*i + 1)
    return total


def approx_cos(x, n):
    total = 0
    for i in range(n):
        total += ((-1)**i * x**(2*i)) / factorial(2*i)
    return total


def approx_cosh(x, n):
    total = 0
    for i in range(n):
        total += (x**(2*i)) / factorial(2*i)
    return total


def approx_sinh(x, n):
    total = 0
    for i in range(n):
        total += (x**(2*i+1)) / factorial(2*i+1)
    return total


# Testing the function
print(approx_sin(3.14, 10))
print(approx_cos(3.14, 10))
print(approx_sinh(3.14, 10))
print(approx_cosh(3.14, 10))

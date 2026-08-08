# calculate sum of numbers from 1 to N.
def calculate_sum(n: int) -> int:
    _sum = 0
    for i in range(1, n+1):
        _sum = _sum+i
    return _sum

# calculate factorial of a number
def calculate_factorial(n: int) -> int:
    fac = 1
    for i in range(1, n+1):
        fac = fac*i
    return fac



# print(calculate_sum(5))
print(calculate_factorial(4))
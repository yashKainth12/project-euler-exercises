#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sqaureTotal(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum**2

def sumSquareIndividual(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2

    return sum

def compute(n):
    return sqaureTotal(n) - sumSquareIndividual(n)

print(compute(100))
        

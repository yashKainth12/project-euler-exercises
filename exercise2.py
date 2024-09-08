#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

count = 0
oldFibonacciNumber = 1
newFibonacciNumber = 1

while newFibonacciNumber <= 4000000:
    if newFibonacciNumber % 2 == 0:
        count += newFibonacciNumber
    # Update Fibonacci numbers
    thirdFibonacciNumber = newFibonacciNumber + oldFibonacciNumber
    oldFibonacciNumber = newFibonacciNumber
    newFibonacciNumber = thirdFibonacciNumber

print(count)
#correct
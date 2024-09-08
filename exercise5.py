#smallest number where each of the numbers 1-20 divides it

def gcd(a,b):
    return max(i for i in range(1, min(int(a), int(b)) + 1) if a % i == 0 and b % i == 0)


def lcm(a,b):
    return (a*b)/gcd(a,b)

def compute():
    num=1
    for i in range(1,21):
        num = lcm(num,i)

    return num

print(compute())

#correct




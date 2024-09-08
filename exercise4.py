#largest palindromic product of 2 3 digit numbers
def isPalindromic(n):
    n = str(n)
    return n == n[::-1]

def largestPalindromic():
    largest_palindromic = 1  # Initialize with 1 or any value smaller than possible palindromic products
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if isPalindromic(product):
                if product > largest_palindromic:
                    largest_palindromic = product

    return largest_palindromic


def compute():
	ans = max(i * j
		for i in range(100, 1000)
		for j in range(100, 1000)
		if str(i * j) == str(i * j)[ : : -1])
	return str(ans)

print(compute())
def factorial(n):
    # Write your code here
    if n==1:
        return 1
    return n*factorial(n-1)

n = int(input().strip())

result = factorial(n)

print(result)
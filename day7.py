
n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

arr.reverse()

for i in arr:
    print(i,end=' ')
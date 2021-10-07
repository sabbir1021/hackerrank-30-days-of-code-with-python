# Day 20: Sorting


n = int(input().strip())
a = list(map(int, input().rstrip().split()))[0:n]
count = 0
for i in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:
            pj_1 = a.pop(j+1)
            pj = a.pop(j)
            a.insert(j,pj_1)
            a.insert(j+1,pj)
            count = count+1
        
print(f'Array is sorted in {count} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[n-1]}')
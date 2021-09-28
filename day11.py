arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
lis = []
for i in range(4):
    for j in range(4):
        v1 = arr[i][j]
        v2 = arr[i][j+1]
        v3 = arr[i][j+2]
        v4 = arr[i+1][j+1]
        v5 = arr[i+2][j]
        v6 = arr[i+2][j+1]
        v7 = arr[i+2][j+2]
        cal = v1 + v2 + v3 + v4 + v5 + v6 + v7
        lis.append(cal)
        
print(max(lis))
        

n = int(input().strip())
b = bin(n)
a = b[2:]
lis = []
count = 0
for i in range(len(a)):
    if a[i] == '1':
        count = count + 1
        if i+1 == len(a):
            lis.append(count)
    else:
        lis.append(count)
        count = 0
        
print(max(lis))
    


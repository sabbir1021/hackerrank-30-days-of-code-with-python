# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d = {}
l = []
d = [map(str,input().split()) for x in range(n)]
d = dict(d)

for j in range(n):
    name = input()
    l.append(name)
 
for x in range(n):
    if l[x] in d.keys():
        c = l[x]
        print(c+'='+d[c])
    else:
        print('Not found')

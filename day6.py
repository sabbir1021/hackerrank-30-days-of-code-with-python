t = int(input())
for k in range(t):
    s = input()
    li = []
    for i in range(0,len(s),2):
        v = s[i]
        li.append(v)
    li.append(' ')
    for j in range(1,len(s),2):
        v = s[j]
        li.append(v)
    result = ''.join(li)
    print(result)

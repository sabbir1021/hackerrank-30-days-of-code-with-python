# problem : Day 14: Scope by Hackerrank


class Difference:
    def __init__(self, a):
        self.__elements = a
    
    def computeDifference(self):
        a = self.__elements
        l =[]
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                sub = abs(a[i]-a[j])
                l.append(sub)
        
        self.maximumDifference =  max(l)

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
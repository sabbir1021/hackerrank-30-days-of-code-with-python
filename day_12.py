class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName, lastName, idNumber,scores):
        super().__init__(firstName,lastName,idNum)
        self.scores = scores
    def calculate(self):
        total = 0
        for i in scores:
            total = total+i
        avr = total / len(scores)
        if avr >= 90 and avr <= 100:
            return 'O'
        if avr >= 80 and avr < 90:
            return 'E'
        if avr >= 70 and avr < 80:
            return 'A'
        if avr >= 55 and avr < 70:
            return 'P'
        if avr >= 40 and avr < 55:
            return 'D'
        if avr < 40:
            return 'T'
    
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

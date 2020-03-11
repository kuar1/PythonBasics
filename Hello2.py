print("Buom")

matrix=[[1,2,3],[4,5,6,['a','b','c','d',[11,12,13]]],[7,8,9]]
print(matrix[1][3][-1])
print(matrix[1][3][4][1])

#methods
#popping

numbers=[1,2,3,4,5,6,7,8]
print(numbers)
numbers.pop()
print(numbers)

empty=[2]
print(empty)
empty.append(23)
print(empty)

name='buom'
### Research
# print('geeks', 'geeks', 'geeks')
# print(string.replace)

days=('monday', 'tuesday', 'wednesday', 'thurday', 'friday', 'saturday', 'sunday')
print(days)
#print(days.append)

numbers[2]=11
print(numbers)

print(days[3])

userName='mark'
password='abc'

myDBvalues=(1, 'mark', 'password', 30, 'male')
un=myDBvalues[1]
print(un)
pss=myDBvalues[2]
print(pss)
### Strict Equality Operator- assaignment operator (if 1 = 1)
if un==userName:
    print('userName true')
else:
    print('userName false')

if pss==password:
    print('password true')
else:
    print('password false')
##Dictionaries

dict=10
print(dict)

myDictionary={'username':'mark', 'password':'abc','age':28,'gender':'male'}
print(myDictionary['age'])
print(myDictionary['password'])
print(myDictionary['gender'])

#x = {
#
#   }
#
#    If an element inside a tuple is mutable, you can modify that element but not the tuple
#    you can append a dictionary
#    you can have a key of anyname and value of

self={'firstName':'Buom', }
#First name, last name, primary schools(school name, population, head teacher, Secondary Schools, Hobbies
#Bonus: Research how to get users input from consile.. ask/take and store
#Multiple Variables

a,b,c = 1,-3,9
if a or b or c > 0:
    print ("True")
else:
    print ("False")

#Bitwise Operator

X = 240     #11110000
Y = X << 2  #rightshift
print (Y)

#Lists1

Name = ['Kenny','Cizario','Marcinho','Tim']

Name.append('Jonathan')
print ("Updated List Name-1:",Name)

#Lists2

Name = ['Antoine', 'Mario', 'De Bruyne']
Age = [23,24,25,26]
Name.extend(Age)
print ("Updated List Name-2:", Name)

#Lists3

Name = ['Antoine', 'Mario', 'De Bruyne', 23]
Name.remove(23)
print ("Updated List Name-3:",Name)

#Lists4

Numbers = [1, 4, 9, 16]
sum = 0
for num in Numbers:
    sum += num
    print (sum)

#Lists5

Name = ['Charles', 'Bowman', 'Smith']
if 'Charles' in Name:
    print ("Yes, the name is in the list.")

#Lists6

Month = ['January', 'March', 'December']
Dates = [99,156,24,57]
print (len(Month))
print (max(Dates))

#Range1

for i in range (10):
    print ("The value is ",i)

#Range2

Genre = ['Pop', 'Glam Metal', 'Alt. Rock']
for i in range(len(Genre)):
    print ("I like", Genre[i])

#Dictionary

Dogs = {"England" : "Golden Retriever", "Japan" : "Japanese Spitz"}
print (Dogs["England"])

#Complex-Numbers1
import cmath
x=29.0
y=77.8

z= complex(x,y)
print (z)

#Sets

My_Set = {1,3}
print(My_Set)

My_Set.add(2)
print(My_Set)

My_Set.add(5)
print("Updated Set Lists:",My_Set)

#String Operations

x ='Hitman\n'
y = '47'
print (len(x))
print (x + y)












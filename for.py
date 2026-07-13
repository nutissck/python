"""
for i in range(10):
    print(i, end=" ")
for i in range(10):
    print(i)

for i in range(3, 10):
    print(i)

for i in range(2, 10, 2):#start, stop, step
    print(i, end=" ")
"""
#Цикл for - простий лічильник    
"""
for i in range(1,6):
    print(i, end=" ")
"""
#перебір елементів списку
"""
people=["Alice","Bob","Charlie"]
print(type(people))
for person in people:
    print(person)
"""
#перебір елементів за індексами
"""
people=["Alice","Bob","Charlie"]
for i in range(len(people)):#довжина списку
    print(people[i])
"""
#зворотній лічильний
"""
for i in range(5, 0, -1):
    print(i, end="")
"""
"""
for i in range(1, 4):
    print(i)
else:
    print("The loop is done")
"""
#continue - пропуск ітерації
"""
for i in range(1, 6):
    if i==3:
        continue
    print(i)
"""
#перебір елементів списку до умови
"""
people=["Alice","Bob","Charlie"]
for person in people:
    if person=="Bob":
        print("Found Bob")
        break """ #зупинка циклу за умови













    

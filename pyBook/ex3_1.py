names = ['fedya', 'kolya', 'vasya', 'misha', 'kostya']
print("Hello " + names[0].title() + '!')
print("Hello " + names[1].title() + "!")
print("Hello " + names[2].title() + "!")
print("Hello " + names[3].title() + "!")
print("Hello " + names[4].title() + "!")
print(names)
print(names.pop())
print(names)
names.append("kirill")
print(names)

print("Hello " + names[0] + "!")
print("Hello " + names[1] + "!")
print("Hello " + names[2] + "!")
print("Hello " + names[3] + "!")
print("Hello " + names[4] + "!")

names.insert(0, 'anya')
names.insert(0, 'petya')
names.append("huylo")

print(names)
print("Hello " + names[0] + "!")
print("Hello " + names[1] + "!")
print("Hello " + names[2] + "!")
print("Hello " + names[3] + "!")
print("Hello " + names[4] + "!")
print("Hello " + names[5] + "!")
print("Hello " + names[6] + "!")
print("Hello " + names[7] + "!")

print("It a pity " + names.pop())
print(names)
print("It a pity " + names.pop())
print(names)
print("It a pity " + names.pop())
print(names)
print("It a pity " + names.pop())
print(names)
print("It a pity " + names.pop())
print(names)
print("It a pity " + names.pop())
print(names)

del names[0]
print(names)

del names[0]
print(names)

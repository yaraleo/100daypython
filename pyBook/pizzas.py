#I made this exercises on 09062018
pizzas = ['pipperoni', 'konskaya', 'ogurechnaya', 'kvadratnaya']
for pi in pizzas:
    print "I like " + pi + " pizza!"
print "\nI really hate pizza!!\n"

print("The first three items of pissa is \n")
print(pizzas[-2:])

def sum(nums):
    total = 0
    for i in nums:
        total += i
    return total

nums = [12,35,42,56,3,4,56,32,13,4]
print sum(nums)


for i in range(1, 21, 2):
    print i

million = []
for i in range(1, 1000001):
    million.append(i)

print(min(million))
print(max(million))
print(sum(million))

triple = [i for i in range(0, 30, 3)]
for i in triple:
    print i

qubs = [i**3 for i in range(1, 10)]

for i in qubs:
    print i

meals = ("Asdfa", "qerw", "rtyerty",'erter')
print(meals)
meals.append("asdfas")

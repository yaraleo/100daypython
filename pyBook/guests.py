guests = ['papa', 'mama', 'vlada', 'dasha', 'vladik']
for guest in guests:
    print("Dear " + guest.title() + " you are invite to dinner!")

print (guests[3].title() + " cant be at dinner")

guests[3] = 'masha'
for guest in guests:
    print("Dear " + guest.title() + " you are invite to dinner!")

print("\nWe want to enlarge our dinner table")
guests.insert(0, "vitek")
guests.insert(3, "sveta")
guests.append("luba")
for guest in guests:
    print("Dear " + guest.title() + " you are invite to dinner!")

print("Sorry we can invite only two guests")
while len(guests) > 2:
    print("We are so sorry that we couldt invite " + guests.pop())

for guest in guests:
    print("We are so glad " + guest.title())

for i in range(0, len(guests)-1):
    del guests[i]
print(guests)

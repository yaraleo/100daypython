# test1 from chapter 15
# book
# http://younglinux.info
#print ("Enter any integer from 1 till 9 > ")
x = int(input("Enter any integer from 1 till 9 > "))
print(x)
if x <= 4:
    s = raw_input("Please enter a string > ")
    n = int(input("Please enter a counter n > "))
    for i in range(1, n+1):
        print(s)
elif x <= 6:
    res = 1
    m = int(input("Please enter a stepen m > 0 > "))
    while m != 0:
        res *= x
        m -= 1
    print (res)
elif x <= 9:
    for i in range(1, 11):
        print(x + i)
else:
    print("Input mistake")

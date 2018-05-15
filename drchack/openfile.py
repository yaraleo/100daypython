fhand = open('words.txt', 'r')
sum = 0
strings = 0
for string in fhand:
    print string[0:len(string)-1] + "\t length " + str(len(string))
    sum += len(string)
    strings += 1
average = sum/strings
print "average", average

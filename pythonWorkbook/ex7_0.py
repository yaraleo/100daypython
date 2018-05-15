fib1 = 0
fib2 = 1
#print(fib1)
#print(fib2)
i = 0
n = 19
while i < n:
    fib_sum = fib1 + fib2
    if i > 2:
        print (fib_sum)
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

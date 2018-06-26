def fract(n):
    if n == 1:
        return 1
    else:
        return n * fract(n - 1)

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

def cowntdown(i):
    print(i)
    if i == 1:
        return 1
    else:
        return cowntdown(i-1)

print(fract(5))
print(sum(5))
cowntdown(10)

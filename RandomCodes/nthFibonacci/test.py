n = int(input())
a = 1
b = 1
c = 2
if n == 1 and n == 2:
    print(1)
else:
    i = 0
    while i < n-2:
        c = a + b
        a = b
        b = c
        i+=1
    print(c)
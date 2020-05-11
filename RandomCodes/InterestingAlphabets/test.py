n = int(input())
i = n-1
count = 1
while i >= 0:
    for j in range(count):
       x = chr(i + j + 65)
       print(x, end = '')
    count+=1
    i-=1
    print()
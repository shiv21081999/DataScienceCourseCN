n = int(input())
for i in range(0, n):
    for j in range(i,i+i+1):
        x = chr(j+65)
        print(x,end = '')
    print()
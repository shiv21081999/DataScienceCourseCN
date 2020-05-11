n = int(input())
for i in range(1, n+1):
   spaces = n - i
   for j in range(spaces):
      print(' ',end = '')
   for j in range(i,i+i):
      print(j, end = '')
   x = i+i-2
   for j in range(i-1):
      print(x,end = '')
      x-=1
   print()
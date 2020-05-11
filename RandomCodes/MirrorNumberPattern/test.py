n = int(input())
for i in range(1, n+1):
   spaces = n - i
   for j in range(spaces):
      print(' ',end = '')
   for j in range(i):
      print(j+1,end = '')
   print()
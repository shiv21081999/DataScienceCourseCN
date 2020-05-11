n = int(input())
for i in range(1, n+1):
   spaces = n - i
   for j in range(spaces):
      print(' ',end = '')
   r = (2*i)-1
   print('*'*r)
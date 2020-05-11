r = int(input())
n = (r//2)+1
for i in range(1, n+1):
   spaces = n - i
   print(' '*spaces, end = '')
   r = (2*i)-1
   print('*'*r)
for i in range(1, n):
   print(' '*i,end = '')
   r = 2*(n-i)-1
   print('*'*r)   
n = int(input())
c = int(input())
if c == 1:
   sum = 0
   for i in range(1, n+1):
      sum += i
   print(sum)
elif c == 2:
   prod = 1
   for i in range(1, n+1):
      prod *= i
   print(prod)
else:
    print(-1)
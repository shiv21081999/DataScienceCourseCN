
def reverse(n):
    rev = 0
    while n > 0:
        r = n%10
        rev = (rev*10) + r;
        n//=10;
    return rev
    pass
		

n=int(input())
result = reverse(n)
print(result)
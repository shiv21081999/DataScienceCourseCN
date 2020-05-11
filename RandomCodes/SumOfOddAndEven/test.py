n = int(input())
even = 0
odd = 0
while n > 0:
    r = int(n%2)
    if int(r%2)==0:
        even+=r
    else:
        odd +=r
    n//=10
print(str(even)+" "+str(odd))
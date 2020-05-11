def checkPalindrome(num):
    rev = 0
    n = num
    while n > 0:
        r = int(n%10)
        rev = (rev*10) + r
        n //= 10
    if num == rev:
        return True
    else:
        return False
	# pass
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')

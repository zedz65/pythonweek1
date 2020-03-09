def three(arg1):
	if arg1 % 3 == 0 and arg1 % 5 ==0:
		return "fizzbuzz"
	elif arg1 % 3 ==0:
		return "fizz"
	elif arg1 % 5 ==0:
		return "buzz"
	else:
	    return "null"

print(three(3))
print(three(5))
print(three(15))
print("2016112258 이용희")

def myfunc(n):
	return lambda a : a*n

mydoubler = myfunc(2)
print(mydoubler(5))

mytripler = myfunc(3)
print(mytripler(5))
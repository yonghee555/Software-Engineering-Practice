print("2016112258 이용희")

def tri_recursion(k):
	if(k > 0):
		result = k +tri_recursion(k - 1)
		print(result)
	else:
		result = 0
	return result

print("The example of recursion ")
tri_recursion(6)
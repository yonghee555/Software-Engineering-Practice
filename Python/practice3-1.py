print("2016112258 이용희")

def func(*args, **kwargs):
	for x in args:
		print(x)
	print('My name :', kwargs["name"], ' & My Age :', kwargs["age"])

func(1, 2, 3, 4, name='YongHee', age=25)
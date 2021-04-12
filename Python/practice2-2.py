print("2016112258 이용희")

fruitlist = ["banana", "Orange", "Kiwi", "cherry"]
print('Original list : ', fruitlist)

fruitlist.reverse()
print("reverse() -> ", fruitlist)

fruitlist.sort()
print("sort() -> ", fruitlist)

fruitlist.sort(key=str.lower)
print("sort(key=str.lower) -> ", fruitlist)
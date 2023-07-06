def map(function, iterable):
	ls = []
	for i in iterable:
		ls.append(function(i))
	return(ls)

def multiply(x):
	return(x*x)

ls = [1,2,3,4,5]

print(map(multiply, ls))
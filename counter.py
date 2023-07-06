def counter():
	counter = 0
	def closure():
		nonlocal counter
		counter += 1
		return(counter)
	return(closure)

func = counter()

print(func()) 
print(func())
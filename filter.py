def filter(func, list):
	ls = []
	for i in list:
		if func(float(i)) == True:
			ls.append(i)
	return(ls)


def adult(x):
  if x < 18:
    return(False)
  else:
    return(True)

ages = input('Enter a list of numbers: ').split(',')

adults = filter(adult, ages)
for i in adults:
	print(i)
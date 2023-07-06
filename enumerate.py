def enumerate(iterable, start = 0):
	ls = []
	for i in range(len(iterable)):
			ls.append((start, iterable[i]))
			start += 1
	return(ls)

ls1 = 'hello'
ls2 = ['one', 'two', True]
print(enumerate(ls1))
print(enumerate(ls2))
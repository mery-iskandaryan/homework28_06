def zip(ls1, ls2):
	ls = []
	for i in range(len(ls1)):
		for j in range(len(ls2)):
			if i == j:
				ls.append((ls1[i],ls2[j]))
	return(ls)

ls1 = input('Enter the first list: ').split(',')
ls2 = input('Enter the secondlist: ').split(',')

print(zip(ls1, ls2))
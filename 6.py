def sum_sq(n):
	list1 = []
	sum = 0
	for i in range(1,n+1):
		sum += i**2
		list1.append(i**2)
	print "all the squares of the first n numbers are", list1
	return sum

def sq_sum(n):
	list2 = []
	sum = 0
	for i in range(1,n+1):
		sum += i
		list2.append(i)
	print " the sum of the first n numbers is", sum
	sum = sum**2
	list2.append(i)
	return sum


x = sum_sq(100)
y = sq_sum(100)
print "the sum of the first 100 numbers squared is", x, "minus the square of the sum of the first 100 numbers", y
print(x-y)

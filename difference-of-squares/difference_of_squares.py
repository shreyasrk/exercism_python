def sum_of_squares(num):
	return sum([i**2 for i in range(1, num+1)])

def square_of_sum(num):
	return sum([i for i in range(1, num+1)])**2

def difference(num):
    return square_of_sum(num) - sum_of_squares(num)


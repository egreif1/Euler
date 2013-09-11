
if __name__ == "__main__":

	past = 1
	cur = 2
	sum = 0
	while cur < 4000000:
		if (cur%2 == 0):
			sum = sum + cur

		new = past+cur
		past = cur
		cur = new

	print(sum)
			

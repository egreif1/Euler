
if __name__ == "__main__":

	# even fibonnaci numbers follow own sequence, so easy to do
	# F(n) = 4*F(n-6)+F(n-3)

	past = 2
	cur = 8
	sum = 0
	while cur < 4000000:
		sum = sum + cur

		new = 4*cur+past
		past = cur
		cur = new

	print(sum)
			

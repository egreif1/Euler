

if __name__ == "__main__":

	# this is brute force.
	# the way to do this problem is just to do
	# math.... add all multiples of 3 + all multiples of 5
	# minus all multiples of 15...
	# (3+9+....) = (n)(n+1)/2... etc.
	sum = 0
	for i in range(1,1000):
		if (i%3 == 0 or i%5 == 0):
			sum = sum+i
	print(sum)


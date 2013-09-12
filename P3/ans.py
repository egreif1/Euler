
import sys

def max_factor(num):

# first divide out two as much as possible
# so we can go up by two each time
	
	max = 0

	while (num%2 == 0):
		num = num/2
		max = 2

	test = 3

	while(num > max):
		if (num%test == 0):
			num = num/test	
			if (test > max):
				max = test
			if (num == 1):
				return max
			test = 3
		else:
			test = test + 2

		# check if we're above, sqrt(num)
		# if so, we're done
		if (test > num^(1/2)):
			return num

	return max


if __name__ == "__main__":

	if(len(sys.argv)<2):
		print("Enter a number")
		sys.exit()

	num = int(sys.argv[1])

	max = 0
	
	ans = max_factor(num)
	print(ans)
	

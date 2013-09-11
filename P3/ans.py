
import sys

def max_factor(num,max):
	factor = first_factor(num)

	if (factor > max):
		max = factor


	num = num/factor


	if (num == 1):
		return max
	else:
		return max_factor(num,max)


def first_factor(num):
	for i in range(2,num+1):
		if (num%i == 0):
			return i


if __name__ == "__main__":

	if(len(sys.argv)<2):
		print("Enter a number")
		sys.exit()

	num = int(sys.argv[1])

	max = 0
	
	ans = max_factor(num,max)
	print(ans)
	

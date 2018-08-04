

def euclid_alg(a, b):
	q = -1
	r = -1
	gcd = 0
	while True:
		r = a % b
		if (b % r == 0):
			gcd = r
			break
		a = b
		b = r
	return gcd

a, b = input("Please enter the 2 integers you'd like to find the gcd for\n").split(' ')


print("The gcd of {} and {} is {}".format(a, b, euclid_alg(int(a), int(b))))
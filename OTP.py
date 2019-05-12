import random

def generate():
	x=""
	for i in range(6):
		x=x+str(random.randint(0,9))
	return x

print('Your One Time Password is : '+generate())	




'''
problem: smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?

'''
import fractions

def compute(givenArg):
	ans = 1
	for i in range(1, givenArg + 1):
		ans *= i // fractions.gcd(i, ans)
	return str(ans)

def main():
	print('this program computes the largest Palidrome product')
	x = int(raw_input('enter a celing: '))
	y = compute(x)
	print(y, 'is evenly divisible by all the numbers from 1 to ', x)
	print('making it the smallest multiple ')

main()
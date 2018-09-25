''' 
problem: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def prime_factors(n):
    factors=[]
    d=2
    while(d*d<=n):
        while(n>1):            
            while n%d==0:
                factors.append(d)
                n=n/d
            d+=1
    return factors


def main():
	print('this program computes a prime factorization of a given input')
	x = int(raw_input('enter a number: '))
	print('the prime factors of ', x, 'are: ')
	print(prime_factors(x))
	print('the largest prime factor of ', x, 'is: ')
	print(max(prime_factors(x)))

main()
	
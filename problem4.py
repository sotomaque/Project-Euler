'''
problem: Largest Palidrome Product

'''

def LPP():
	palidromes = []
	#loop through all three digit numbers
	for i in range(100,1000):
		for j in range(100,1000):
			#convert product into strings to quickly check if they are palidromes using pythons
			#[::-1] notation
			if (str(i*j) == str(i*j)[::-1]):
				palidromes.append(i*j)

	#return largest palidrome
	return max(palidromes)

def main():
	print('this program computes the largest Palidrome product')
	print(LPP())

main()
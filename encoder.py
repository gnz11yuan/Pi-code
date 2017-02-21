#!/usr/bin/env python
import random


if __name__ == "__main__":

	ok=False
	while ok==False:
		ok=True
		intext = str(input("insert text: "))
		intext = intext.upper()
		listText=list(intext)
		for i in range (0,len(listText)):
			if (listText[i].isalpha()==False):
				if(listText[i] != " "):
					ok=False
		if ok==False:
			print("The program can only encode letters. Retry.")


	alf="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	alf=list(alf)
	pi="31415926535897932384626433"
	pi=list(pi)
	occ="11121111223121332422233356"
	occ=list(occ)


	sub=[]
	#monoalphabetic substitution
	for i in range (0,len(listText)):
		if(listText[i]==" "):
			sub+="0"
		else:
			sub+=pi[alf.index(listText[i])]
			sub+=occ[alf.index(listText[i])]


	fibonacci_numbers = [1, 1]
	i=2
	while (len(''.join(map(str,fibonacci_numbers)))<len(sub)):
		fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
		i=i+1
	fiboStr=''.join(map(str,fibonacci_numbers))[:len(sub)]
	
	
	
	numfib = int(fiboStr)
	numText = int(''.join(map(str,sub)))
	numText=numText+numfib
	textfinal=[]

	for digit in str(numText):
		textfinal+=digit


	a=random.randint(1, len(listText))

	for i in range (0,a):
		b=random.randint(0, len(listText))
		textfinal.insert(b,random.choice(alf).lower())
	print(''.join(map(str,textfinal)))




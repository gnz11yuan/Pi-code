#!/usr/bin/env python
def delete_alpha(text): #deletes letters
	i=0
	while (i<len(text)):

		if (text[i].isalpha() == True):
			del text[i]
		else:
			i=i+1
	return text

def matching(a,b, occ, pi, alf):
	for i in range (0,len(alf)):
		if a == pi[i] and b==occ[i]:
			return alf[i]
	return "error"

if __name__ == "__main__":
	intext = str(input("insert text: "))

	listText=[]
	alf="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	pi="31415926535897932384626433"
	occ="11121111223121332422233356"

	listText = delete_alpha(list(intext))
	
	#generating fibonacci
	fibonacci_numbers = [1, 1]
	i=2
	while (len(''.join(map(str,fibonacci_numbers)))<len(listText)):
		fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
		i=i+1
	
	fiboStr=''.join(map(str,fibonacci_numbers))[:len(listText)]

	numfib = int(fiboStr)
	numText = int(''.join(map(str,listText)))
	print(numText)

	if (numText - numfib) > 0:
		numText=numText-numfib
	else:
		fiboStr=''.join(map(str,fibonacci_numbers))[:-1]
		numfib = int(fiboStr)
		numText=numText-numfib

	print(numfib)
	print(numText)
	

	textfinal=""
	
	for digit in str(numText):
		#delete 0s
		if digit == '0':
			textfinal+=(" ")
		else:
			textfinal+=digit
	seq=[]
	seq = textfinal.split(" ")

	decrypted = []

	for word in seq:
		for k in range (0, len(word)-1, 2):
			decrypted.append(matching(word[k],word[k+1],list(occ),list(pi),list(alf)))
		print(''.join(map(str,decrypted)) + " ")
		decrypted=[]


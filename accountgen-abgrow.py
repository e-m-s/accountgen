# Modulo 11 rule - vyhláška č. 169/2011 Sb.
# Číslo ABCDEFGHIJ (viz výše uvedená tabulka) je zajištěno pomocí modulo 11, pokud je součet S beze zbytku dělitelný 11, přičemž platí, že
# S = J*1 + I*2 + H*4 + G*8 + F*5 + E*10 + D*9 + C*7 + B*3 + C*7 + B*3 + A*6

DIGITS = 9
arr = [ 0 ] * DIGITS
nonZeroes = 0

def reset():
	global arr
	global nonZeroes
	
	arr = [ 0 ] * DIGITS
	arr[0] = 1
	arr[DIGITS-1] = 1
	nonZeroes = 2

def increaseAbc(index, cGrow):
	global arr
	global nonZeroes
	
	if index < 0:
		exit()
	if arr[index] == 9  or (cGrow and index == 2 and arr[index] == 7):
		arr[index] = 0
		nonZeroes = nonZeroes - 1
		increaseAbc(index-1, cGrow)
	else:
		newVal = arr[index]+1
		arr[index] = newVal
		if newVal == 1:
			nonZeroes = nonZeroes + 1
	arr[3] = arr[6] = arr[0]
	arr[4] = arr[7] = arr[1]
	if cGrow:
		increment = 1
	else:
		increment = 0
	arr[5] = arr[2] + increment
	arr[8] = arr[5] + increment

def checkMod11():
	#s = arr[9]*1 + arr[8]*2 + arr[7]*4 + arr[6]*8 + arr[5]*5 + arr[4]*10 + arr[3]*9 + arr[2]*7 + arr[1]*3 + arr[0]*6;
	s = arr[8]*1 + arr[7]*2 + arr[6]*4 + arr[5]*8 + arr[4]*5 + arr[3]*10 + arr[2]*9 + arr[1]*7 + arr[0]*3;
	# print(s, " ", s % 11, " nonZeroes: ", nonZeroes)
	return s % 11 == 0

def printAccount():
	i = 0
	output = ""
	
	for i in range(DIGITS):
		output = output + str(arr[i])

	print(output)


def palindrome():
	global trailingZeroes
	
	low = trailingZeroes
	high = MAX_DIGITS
	
	print(low, " ", high)
	while arr[low] == arr[high] and low < high:
		low = low + 1
		high = high - 1
		print(low, " ", high)
	
	return low >= high


length = len(arr)
reset()
while True:
	increaseAbc(2, True)
	if checkMod11() and nonZeroes >= 2:
		printAccount();

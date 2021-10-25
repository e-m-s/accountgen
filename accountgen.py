MAX_DIGITS = 10
LIMIT_DIGITS = 9

arr = [ 0 ] * MAX_DIGITS
arr[MAX_DIGITS-LIMIT_DIGITS] = 1
arr[MAX_DIGITS-1] = 1
if (LIMIT_DIGITS != 1):
	nonZeroes = 2
else: 
	nonZeroes = 1
trailingZeroes = MAX_DIGITS-LIMIT_DIGITS

def increase(index):
	global arr
	global nonZeroes
	global trailingZeroes
	
	if index < MAX_DIGITS - LIMIT_DIGITS:
		exit()
	if arr[index] == 9:
		arr[index] = 0
		if trailingZeroes >= index:
			trailingZeroes = index-1
		nonZeroes = nonZeroes - 1
		increase(index-1)
	else:
		newVal = arr[index]+1
		arr[index] = newVal
		if newVal == 1:
			nonZeroes = nonZeroes + 1

# Kontroluje tvar AB(c)AB(c+1)AB(c+2)
def checkABgrow():
	global arr
	result = (
		arr[1] == arr[4] 
		and arr[1] == arr[7] 
		and arr[2] == arr[5] 
		and arr[2] == arr[8] 
		and arr[3] == arr[6]-1 
		and arr[3] == arr[9]-2
	)
	return result

def checkMod11():
	s = arr[9]*1 + arr[8]*2 + arr[7]*4 + arr[6]*8 + arr[5]*5 + arr[4]*10 + arr[3]*9 + arr[2]*7 + arr[1]*3 + arr[0]*6;
	# print(s, " ", s % 11, " nonZeroes: ", nonZeroes)
	return s % 11 == 0

def printAccount():
	global trailingZeroes
	
	i = trailingZeroes
	output = ""
	
	while i < 10:
		output = output + str(arr[i])
		i = i+1
	
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
while True:
	increase(length - 1)
	if trailingZeroes == 1 and checkABgrow():
		# printAccount()
		if checkMod11() and nonZeroes >= 2:
			printAccount();

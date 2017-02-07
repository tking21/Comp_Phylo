import datetime
import random
import numpy

#Section 2a
def between ( min, max ):
# a function that calculates the factorial of a set of numbers (max to min)
	answer = 1
	for num in range (min, max+1): 
		# a loop that creates a list of all the number from min to the max number submitted and multiplies each number in the list together
		answer = answer * num 
	return (answer)
	
#print(between (3, 7)) --> checking to make sure that the function works properly 		
		
def binomialA (n, k ):
#a function that calculates the binomial coefficient without simplification  
	#print (str(n) + " choose " + str(k) + " with method A")
	top = between (1, n)
	bottom1 = between (1,k)
	bottom2 = between (1, n-k)
	totalBottom = bottom1 * bottom2
	#print(top)
	#print(bottom1)
	#print(bottom2)
	#print(totalBottom)
	return (top / totalBottom)

def binomialB (n, k ):
#a function that calculates the binomial coefficient with simplification 
	#print (str(n) + " choose " + str(k) + " with method B")
	min = (n-k) +1
	top = between(min, n)
	bottom = between (1,k)
	#print(top)
	#print(bottom)
	return (top / bottom)

def binomail_A_Runs ():
	startTime = datetime.datetime.now()
	(binomialA (7,3))
	(binomialA (43,7))
	(binomialA (16,4))
	(binomialA (25,12))
	(binomialA (44,20))
	(binomialA (32,17))
	(binomialA (10,3))
	(binomialA (32,25))
	(binomialA (45,16))
	(binomialA (54,8))
	(binomialA (77,23))
	elapsedTime = datetime.datetime.now() - startTime
	#print ("Method 2a took " + str(elapsedTime) + " to run.")
	
def binomail_B_Runs ():
	startTime = datetime.datetime.now()
	binomialB (7,3)
	binomialB (43,7)
	print(binomialB (16,4))
	print(binomialB (25,12))
	print(binomialB (44,20))
	print(binomialB (32,17))
	print(binomialB (10,3))
	print(binomialB (32,25))
	print(binomialB (45,16))
	print(binomialB (54,8))
	print(binomialB (77,23))
	elapsedTime = datetime.datetime.now() - startTime
	print ("Method 2B took " + str(elapsedTime) + " to run.")
	
#binomail_A_Runs () #both functions used to test the speed of each function, used to determine which method was faster
#binomail_B_Runs ()

def pmf (p,n,k):
#function that calculates the prob mass function 
	bin = binomialB (n,k)
	#print ( bin * pow(p,k) * pow(1-p, n-k))
	return ( bin * pow(p,k) * pow(1-p, n-k))
	
#pmf (0.3 , 7,3)

#section 2a - part 5
pVals = numpy.arange(0.1,1.1,0.1)			#generate a list of random numbers that will be used for p values
kVals = [random.randrange(1,10) for _ in range (10)]		#generate a list of random number that will be used for k values

def discrete (pVals, kVals):
#function makes a empty list (prob), pulls k and p values from the list passed to it, calculates the pmf for corresponding values and saves them to the list prob
	prob = []
	for x in range(0,10):
		prob.append(pmf(pVals[x], 15, kVals[x]))
		
	#print(prob)
	return (prob)

print(kVals)
print(pVals)
discrete(pVals, kVals)
	
	
#section 2b	
def hillClimb (p, n, k):
#function that determines the ML by climbing up a likelihood surface and return the value of the parameter that maximizes the likelihood
	diff = 0.1
	pCurr = p
	
	while ( diff > 0.001):
		L_pCurr = pmf(pCurr,n,k)
		L_pUp = pmf (pCurr+diff, n,k)
		L_pDown = pmf (pCurr-diff, n,k)
		
		while ( L_pUp > L_pCurr ):
			pCurr = pCurr + diff
			L_pCurr = pmf(pCurr,n,k)
			L_pUp = pmf (pCurr+diff, n,k)
			L_pDown = pmf (pCurr-diff, n,k)
	
		while (L_pDown > L_pCurr ):
			pCurr = pCurr - diff
			L_pCurr = pmf(pCurr,n,k)
			L_pUp = pmf (pCurr+diff, n,k)
			L_pDown = pmf (pCurr-diff, n,k)
	
		diff = diff / 2	
		
	return (pCurr)

#print(hillClimb (0.3, 20, 4))


#section 2c
def LRCut (p):
	pCurr = p
	pVals = [random.random() for _ in range (101)]
	nVals = [random.randrange(51,100) for _ in range (101)]
	kVals = [random.randrange(1,50) for _ in range (101)]
	#print(pVals)
	#print(nVals)
	#print(kVals)
	
	lVals = []
	for x in range (0,101):
		#print(x)
		#print(pVals[x])
		#print(nVals[x])
		#print(kVals[x])
		lVals.append(pmf(pVals[x],nVals[x],kVals[x]))
		
	#print(lVals)
		
LRCut (0.3)









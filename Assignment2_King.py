import datetime
import random
import numpy

#Section 2a
def between ( min, max ):
	"""
	a function that calculates the factorial of a set of numbers (max to min)
	"""
	answer = 1
	for num in range (min, max+1): 
		# a loop that creates a list of all the number from min to the max number submitted and multiplies each number in the list together
		answer = answer * num 
	return (answer)
	
#print(between (3, 7)) #--> checking to make sure that the function works properly 		
		
def binomialA (n, k ):
	"""
	a function that calculates the binomial coefficient without simplification
	"""
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
	"""
	a function that calculates the binomial coefficient with simplification
	"""
	#print (str(n) + " choose " + str(k) + " with method B")
	min = (n-k) +1
	top = between(min, n)
	bottom = between (1,k)
	#print(top)
	#print(bottom)
	return (top / bottom)

def binomail_A_Runs ():
	"""
	function used to test the difference in run times between binomialA and binomialB
	"""
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
	print ("Method 2a took " + str(elapsedTime) + " to run.")
	
def binomail_B_Runs ():
	"""
	function used to test the difference in run times between binomialA and binomialB
	"""
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
	
#both functions used to test the speed of each function, used to determine which method was faster
#binomail_A_Runs () 
#binomail_B_Runs ()

def pmf (p,n,k):
	"""
	function that calculates the prob mass function (see equation 3.3.5)
	"""
	bin = binomialB (n,k)
	#print ( bin * pow(p,k) * pow(1-p, n-k))
	return ( bin * pow(p,k) * pow(1-p, n-k))
	
#print(pmf (0.3 , 7,3))

#section 2a - part 5
pVals = numpy.arange(0.1,1.1,0.1)			#generate a list of random numbers that will be used for p values
kVals = [random.randrange(1,10) for _ in range (10)]		#generate a list of random number that will be used for k values

def sample (pVals, kVals):
	"""
	samples from an arbitrary discrete distribution
	"""
	p = numpy.arange(0.1,1.1)
	 if p <= pVals[0]:
	 	return kVals[0]
	 elif p <= pVals[1]:
	 	return kVals[1]:
	 elif p <=  pVals[2]:
	 	return kVals[2]:
	 else 
	 	return kVals[3]:

#print(kVals)
#print(pVals)
#sample(pVals, kVals)
	
	
#section 2b	
def hillClimb (p, n, k):
	"""
	function that determines the ML by climbing up a likelihood surface and return the value of the parameter that maximizes the likelihood
	"""
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

print(hillClimb (0.3, 10, 5))


#section 2c
def LRCut (p):
	"""
	a function that calculates the likelihood ratios for a given group of simulated trails, is passed a known p value
	"""
	
	#generate a list of 100 k values to signify 100 simulated trials
	kVals = [random.randrange(0,5) for _ in range (101)] #generate a list of 100 k values to signify 100 simulated trials
	print(kVals)
	n = 5 	
	
	MlVals = []
	LR = [] 
	p values using hill climb function  
	for k in kVals:
		print(k)
		print(p)
		print(n)
		if n == k:
			MlVals.append(1)
		elif k == 0:
			MlVals.append(0)
		else:	
			MlVals.append(hillClimb(p,n,k)
	
	print(MlVals)
	
	#calculate likelihood ratios and save to LR list - comapring likelihood values using known p (passed to the function) to those determined using hill climb function 
	for  spot in range (0,101) :
		LR.append(pmf (MlVals[spot], n,kVals[spot]) /pmf (p,n,kVals[spot]))
	
	#print(LR)
	sortedLR = sorted(LR)
	#print(sortedLR)
	print("for this dataset, the LR cutoff is " + str(sortedLR[95]))
	
LRCut (0.3)







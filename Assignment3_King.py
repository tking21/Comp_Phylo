from scipy.stats import binom, uniform
import numpy 
import random 
#from pymc3 import traceplot as tp 
import matplotlib.pyplot as plt

flips = ["H", "H", "H", "H", "H", "H", "H", "T", "T", "H"] 		#defining data, determining the number of heads (successes)
successes = sum([1 for _ in flips if _ == "H" ])				#and  the total number of flips (n) --> for binomial 
total_flips = len(flips)


print(successes)
print(total_flips)

def like (successes, total_trails, prob, testingPrior = False):
	"""
	A fucntion that calculates the likelihood of observing _ successes in n trials with a
	known p value of 'prob'
	"""
	if testingPrior :
		return 1
	if prob < 0:
		return 0
	elif prob > 1:
		return 0
	else:
		return binom.pmf(successes, total_trails, prob)

print("The likelihood is " + str(like(successes, total_flips, 0.1)))
print("The likelihood is " + str(like(successes, total_flips, 0.2)))
print("The likelihood is " + str(like(successes, total_flips, 0.3)))
print("The likelihood is " + str(like(successes, total_flips, 0.4)))
print("The likelihood is " + str(like(successes, total_flips, 0.5)))
print("The likelihood is " + str(like(successes, total_flips, 0.6)))
print("The likelihood is " + str(like(successes, total_flips, 0.7)))
print("The likelihood is " + str(like(successes, total_flips, 0.8)))
print("The likelihood is " + str(like(successes, total_flips, 0.9)))


		
def prior (prob): 
	"""
	A function that calculates the prior using the prob density function
	"""
	return uniform.pdf(prob) #uniform, uniformative prior 

print("The prior is " + str(prior(0.8)))
	
def posterior (successes, total_trials, prob):
	"""
	A function that calculates the unnormalized posterior density by multiplying the prior times the likelihood
	"""
	posterior = prior(prob) * like(successes, total_trials, prob)
	return posterior

print("The posterior is " + str(posterior(successes, total_flips, 0.8)))

def drawValues (total_trials, prob, simulations):
	"""
	A function that draws new values (based on the number of simulation) from a binomial distribution
	based on its parameters (prob of success and number of trials)
	"""
	return numpy.random.binomial (total_trials, prob, simulations)

print(drawValues(10,0.8, 10))
	
def acceptReject (proposed_posterior, current_posterior):
	""" A function that either returns true to accept or false to reject a move to a proposed state
	"""
	#calculate the posterior ratio of the proposed and current states  
	r = proposed_posterior / current_posterior 	
	
	#if r is greater than 1, always accept; if less than 1, accept r% of the time 
	if r >= 1:
		return True
	else:
		rand_num = random.uniform(0,1)
		if rand_num <= r:
			return True
		else:
			return False

print("This answer should be True " + str(acceptReject (.8,.2)))
print("This answer should be Fasle or True " + str(acceptReject (.2,.8)))
print("This answer should be Fasle or True " + str(acceptReject (.2,.8)))
print("This answer should be Fasle or True " + str(acceptReject (.2,.8)))
print("This answer should be Fasle or True " + str(acceptReject (.2,.8)))
print("This answer should be Fasle or True " + str(acceptReject (.2,.8)))
	
priors = []
likelihoods = []
posteriors = []
kVals = []

def runChain (generations, total_trials, prob, kVals, priors, likelihoods, posteriors):
	"""
	A function to run the MCMC chain
	"""
	current_state = drawValues (total_trials, prob, 1) 
	print(current_state)
	
	for spot in range(0,generations):
	
		#calculate the posterior prob of the proposed state and current state 
		kVals.append(current_state)
		priors.append(prior(prob))
		likelihoods.append(like(current_state, total_trials, prob))
		current_posterior = posterior(current_state, total_trials, prob)
		proposed_state = drawValues (total_trials, prob, 1)
		proposed_posterior = posterior(proposed_state, total_trials, prob)
		
		if acceptReject (proposed_posterior, current_posterior):
			posteriors.append(proposed_posterior)
			current_state = proposed_state 
		else:
			posteriors.append(current_posterior)
		if spot % 10 == 0:
			print (str(spot)+ " of " +str(generations)+ " generations. the current posterior desnsity is " + str(current_posterior))

runChain(1000, 20, .8, kVals, priors, likelihoods, posteriors)
print(kVals)
#print(posteriors)
#print(likelihoods)

#generating traceplots
#tp(posteriors);
#tp(likelihoods);
#tp(priors);
#tp(kVals);


#generating histograms
numBins = 50
n, bin, patches = plt.hist(posteriors, numBins, normed=1, facecolor='blue', alpha=0.75)
plt.xlabel('Posterior Densities')
plt.ylabel('Frequency')
plt.axis([0, 20, 0, a.all(n)+0.1])
plt.grid(True)

n, bin, patches = plt.hist(priors, numBins, normed=1, facecolor='blue', alpha=0.75)
plt.xlabel('Prior')
plt.ylabel('Frequency')
plt.axis([1, 20, 0, a.all(n)+0.1])
plt.grid(True)

n, bin, patches = plt.hist(likelihoods, numBins, normed=1, facecolor='blue', alpha=0.75)
plt.xlabel('Likelihood')
plt.ylabel('Frequency')
plt.axis([0, 20, 0, a.all(n)+0.1])
plt.grid(True)

n, bin, patches = plt.hist(kVals, numBins, normed=1, facecolor='blue', alpha=0.75)
plt.xlabel('Successes')
plt.ylabel('Frequency')
plt.axis([0, 20, 0, a.all(n)+0.1])
plt.grid(True)






















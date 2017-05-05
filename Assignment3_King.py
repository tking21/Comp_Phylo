from scipy.stats import binom, uniform, norm
import numpy 
import random 
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
		
def prior (prob): 
	"""
	A function that calculates the prior using the prob density function
	"""
	return uniform.pdf(prob) #uniform, uniformative prior 
	
	
def posterior (successes, total_trials, prob):
	"""
	A function that calculates the unnormalized posterior density by multiplying the prior times the likelihood
	"""
	posterior = prior(prob) * like(successes, total_trials, prob)
	return posterior
	
	
def drawValues (prob, stdv):
    """
    A function that draws new values (based on the number of simulation) from a binomial distribution
    based on its parameters (prob of success and number of trials)
    """
    new_p = norm(prob, stdv).rvs()
    return new_p
    
    
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

priors = []
likelihoods = []
posteriors = []
pVals = []

def runChain (generations, successes,total_trials, prob, stdv, priors, likelihoods, posteriors, pVals):
    """
    A function to run the MCMC chain
    """
    current_state = prob 
    print(current_state)
    
   
    for spot in range(0,generations+1): 
    	priors.append(prior(prob))
        likelihoods.append(like(successes, total_trials, current_state))
        
        #calculate the posterior prob of the proposed state and current state
        current_posterior = posterior(successes, total_trials, current_state)
        proposed_state = drawValues (current_state, stdv)
        proposed_posterior = posterior(successes, total_trials, proposed_state)
        
        if acceptReject (proposed_posterior, current_posterior):
            posteriors.append(proposed_posterior)
            pVals.append(proposed_state)
            current_state = proposed_state 
        else:
            posteriors.append(current_posterior)
            pVals.append(current_state)
        if spot % 10 == 0:
            print (str(spot)+ " of " +str(generations)+ " generations. the current posterior desnsity is " + str(current_posterior))
            print ("the current state of p is " + str(current_state))


runChain(1000, successes ,total_flips, .5, 0.1, priors, likelihoods, posteriors, pVals)



#plot histogram of posterior values 
n, bin, patches = plt.hist(posteriors, 50, normed=1, facecolor='blue', alpha=0.75)
plt.xlabel('Posterior Densities')
plt.ylabel('Frequency')
plt.axis([0, 1, 0, 100])
plt.grid(True)
plt.show()

#plot histogram of pVals
n, bin, patches = plt.hist(pVals, 50, normed=1, facecolor='blue', alpha=0.75)
plt.xlabel('p values')
plt.ylabel('Frequency')
plt.axis([0, 1, 0, 5])
plt.grid(True)
plt.show()

#plot histogram of likelihood values 
n, bin, patches = plt.hist(likelihoods, 50, normed=1, facecolor='blue', alpha=0.75)
plt.xlabel('Likelihoods')
plt.ylabel('Frequency')
plt.axis([0, 1, 0, 100])
plt.grid(True)
plt.show()


#plot trace plot of posterior values 
plt.plot(posteriors)
plt.title('Posterior Densities')
plt.show()

#plot trace plot of pVals 
plt.plot(pVals)
plt.title('p values')
plt.show()

#plot trace plot of likelihood values
plt.plot(likelihoods)
plt.title('Likelihoods')
plt.show()































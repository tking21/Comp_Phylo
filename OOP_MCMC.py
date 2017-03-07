import random

class mChain(object):
    """ 
    This class defines and runs a MC 
    """

    def __init__(self, nSteps, states, matrix, sampled):
        """
        intitialize all variables of interest
        """
        self.nSteps = nSteps
        self.states = states
        self.matrix = matrix
        self.sampled = sampled

    def run(self, nSteps, states, matrix, sampled):
        """
        Run the chain 
        """
        #start at some random state within the "states" list 
        current_state = random.choice(states)
        sampled.append(current_state)
        #print("current state = " + str(current_state))
        
        #determing what index this state correlates to 
        current_index = states.index(current_state)
        #print(current_index)
       
        #doing the same for proposed state
        
        for _ in range(0,nSteps):
            #print(_)
            proposed_state = random.choice(states)
            #print(proposed_state)
            proposed_index = states.index(proposed_state)
            #print(proposed_index)
        
            if matrix[current_index][proposed_index] == 1:
            	#print(matrix[current_index][proposed_index])
                current_state = proposed_state
                sampled.append(current_state)
                current_index = proposed_index
                
            
            elif matrix[current_index][proposed_index] == 0:
                sampled.append(current_state)
            
            else:
                rand_num = random.uniform(0,1)
                #print(rand_num)
                if rand_num <= matrix[current_index][proposed_index]:
                    current_index = proposed_index
                    sampled.append(proposed_state)
                else:
                    sampled.append(current_state)
                    
        print(sampled)
        
    def clear():
        """
        clear the chain 
        """
        sampled = []
    
    

states = ["sunny", "rainy"]
Q = [[0,1],[0.7,0.3]]
sampled= []


test = mChain(10, states, Q, sampled)
test.run(test.nSteps, test.states, test.matrix, test.sampled)
   
	
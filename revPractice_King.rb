#load data 
contData <- readContinuousCharacterData("data/primates_lhtlog.nex")


#target body mass specifically
contData.excludeAll()
contData.includeCharacter(3)

#load time tree
treeArray <- readTrees("data/primates.tree")
psi <- treeArray[1]

#moves and rate parameter
mvi = 0
logSigma ~ dnUniform(-5,5)
sigma := 10^logSigma

#set moves on rate parameter
moves[++mvi] = mvSlide(logSigma, delta=1.0, tune=true, weight=2.0)


#assign random variable to the model and allow the  model to sample values for body mass for extant taxa
logmass ~ dnPhyloBrownianREML(psi, branchRates=1.0, siteRates=sigma, nSites=1)
logmass.clamp( contData ) #clamp data to the varible 

#make model object
mymodel = model(sigma)

monitors[1] = mnScreen(printgen=10, sigma)
monitors[2] = mnFile(filename="output/primates_mass_REML.log", printgen=10, separator = TAB,sigma)
    
#run analysis 
mymcmc = mcmc(mymodel, monitors, moves)
mymcmc.burnin(generations=10000,tuningInterval=500)
mymcmc.run(100000)



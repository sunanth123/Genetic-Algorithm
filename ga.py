import random
from Queue import PriorityQueue


##Sunanth Sakthivel
##CS541 Program 2
##this program is a genetic algorithim that will find the solution to the knapsack problem. Note that the 
##optimality of the solution will depend on the number of iterations and population size of the sample.


MaxWeight = 100 ##max weight for knapsack problem
population = 16 ##the population size (will always remain constant)
objects = [[45,3], [40,5], [50,8], [90,10]] ##this is a list of lists (first element is weight, second is value)
PopulationSize = [] ##this will hold the current population members
NumIterations = 100 ##number of breeding, mutation and death cycles

##this function will return the fitness value of a member in the population based on their list 
def fitnessfunction(templist,objects,MaxWeight):
    totalvalue = 0
    totalweight = 0

    for i in range(len(templist)):
        if templist[i] == 1:
            totalvalue += objects[i][1]
            totalweight += objects[i][0]

    if totalweight > MaxWeight:
        totalvalue = 0

    return totalvalue

##this function will return the total weight of a member in the population based on their list
def weight(templist,objects):
    totalweight = 0
    for i in range(len(templist)):
        if templist[i] == 1:
            totalweight += objects[i][0]

    return totalweight


##randomize the initial population with members
for i in range(population):
    templist = []
    for i in range(len(objects)):
        templist.append(random.randint(0,1))

    fitness = fitnessfunction(templist,objects,MaxWeight)
    PopulationSize.append((fitness,templist))

##this is the breeding, mutation and death cycle iterations
for x in range(NumIterations):

    ##determine which two parents in current population will breed
    parent1 = random.randint(0,population-1)
    parent2 = parent1
    while parent1 == parent2:
        parent2 = random.randint(0,population-1)
    
    ##determine where crossover will happen
    crossover = random.randint(1,len(objects)-1)

    tempchild1 = PopulationSize[parent1][1]
    tempchild2 = PopulationSize[parent2][1]
    child1 = []
    child2 = []

    ##apply crossover
    for i in range(crossover):
        child1.append(tempchild1[i])
        child2.append(tempchild2[i])
    for i in range(crossover,len(objects)):
        child1.append(tempchild2[i])
        child2.append(tempchild1[i])

    ##apply mutation on random gene (if selected by chance) on the two children
    mutationchance = random.randint(0,1)
    if mutationchance == 1:
        mutation = random.randint(0,len(objects)-1)
        if child1[mutation] == 0:
            child1[mutation] = 1
        else:
            child1[mutation] = 0

    mutationchance = random.randint(0,1)
    if mutationchance == 1:
        mutation = random.randint(0,len(objects)-1)
        if child2[mutation] == 0:
            child2[mutation] = 1
        else:
            child2[mutation] = 0


    ##get the fitness values of the two children
    fitness1 = fitnessfunction(child1,objects,MaxWeight)
    fitness2 = fitnessfunction(child2,objects,MaxWeight)
    

    PopulationSize.append((fitness1, child1))
    PopulationSize.append((fitness2, child2))

    queue = PriorityQueue()
    
    ##load memebers of population into priority queue and pop off the lowest valued members
    ##this is the Killing process to keep total population size the same constant number
    for i in range(len(PopulationSize)):
        queue.put((PopulationSize[i][0], PopulationSize[i]))

    queue.get()[1]
    queue.get()[1]
    PopulationSize = []
    while queue.qsize():
        PopulationSize.append(queue.get()[1])


max = 0
index = 0

##get the best member and display its values
for member in PopulationSize:
    if max < member[0]:
        max = member[0]

for i in range(len(PopulationSize)):
    if PopulationSize[i][0] == max:
        index = i
        break

totweight = weight(PopulationSize[index][1],objects) 

print ""
print "Best remaining member of population:"
print (PopulationSize[index])
print ""
print "Actual weight: %d" % totweight
print "Value: %d" % (PopulationSize[index][0])


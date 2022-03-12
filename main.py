###########################################################
############# The Pyramid Scheme Algorithm ################
###########################################################

################
### Overview ###
################
"""
This code assumes you're a part of an MLM/Pyramid Scheme trying to recruit others. 
If you take in n amount of people (per person), and then those people take in n amount 
of people - which continues the cycle - then you'd be looking at a finite cycle of 
how many people you can bring in total: basically until the entire population is 
working for the same MLM/Pyramid Scheme. The code below shows how quickly a pyramid 
scheme stops.
"""

##############################################
### Legend of variables and what they mean ###
##############################################
"""
populationOnEarth = the total population you put in
n = number of people each person has to recruit

cycle = the round of people. For instance, if you recruit 3 people, then 
there are 2 rounds (yourself, and the three people you recruited). If those 3 
people recruit 3 people each, then that is another round (or cycle)

listLevels = the list of each round of recruits (i.e. [1, 3, 9, 27]) first person may 
get 3 people, those 3 people get 3 each (9), those 9 get 3 each (27), etc

levelRecruited = the current round of how many are there (round 3 in the above list 
would be 9 people)
"""
###########################
##### the work itself #####
###########################

popPeople = int(input("What is the population you wish to use? "))
requiredRecruits = int(input("How many people does each person have to recruit? "))

commission = int(input("How much will each person's commission be? "))
percent = float(input("What is the percentage that will be deducted from each level's salary? "))

class PyramidSchemers():
  def __init__(self, populationOnEarth=popPeople, n=requiredRecruits):
    pop = "{:,}".format(populationOnEarth)
    cycle = 0
    levelRecruited = 0
    listLevels = []
    
    self.pop = pop
    self.cycle = cycle
    self.levelRecruited = levelRecruited
    self.listLevels = listLevels
    
    while sum(listLevels) < populationOnEarth:
      self.levelRecruited = n ** self.cycle
  
      if sum(self.listLevels) >= populationOnEarth:
        break
      elif sum(self.listLevels) < populationOnEarth:
        self.cycle += 1
        self.listLevels.append(self.levelRecruited)
  
    self.listLevels.pop()
    total = sum(self.listLevels)
    ftotal = "{:,}".format(total)
    self.ftotal = ftotal
  
  ################
  ### Payments ###
  ################
  
  def payment(self, pay=commission, fee=percent):
    money = 0
    levelPayments = []
    hierarchy_of_payments = {}
    
    self.money = money
    self.levelPayments = levelPayments
    self.hierarchy = hierarchy_of_payments
    
    for level in self.listLevels:
      self.money = (pay * level)
      self.money = self.money - (self.money * fee)
      self.levelPayments.append(self.money)

    self.levelPayments.reverse()
    self.levelPayments.pop() # forget the first person bc they make no salary alone
    
    for payment in self.levelPayments:
      fpayment = "{:,}".format(payment)
      self.hierarchy[f'Tier {self.levelPayments.index(payment) + 1}:'] = ("$" + fpayment)

    return self.hierarchy

pyra = PyramidSchemers()
print(pyra.payment()) 

"""
Recall that pyramid schemes require people to further the chain of income. The more recruits,
the better the scheme. Most people will fall around the higher tiers (the ones that make 
the least amount of money), and end up losing most or all of their money trying to reinvest
in the recruitment process.
"""
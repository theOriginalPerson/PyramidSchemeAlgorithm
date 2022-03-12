###########################################################
############# The Pyramid Scheme Algorithm ################
###########################################################

################
### Overview ###
################
"""
This code assumes you're a part of an MLM/Pyramid Scheme trying to recruit others. If you take in n amount of people (per person), and then those people take in n amount of people - which continues the cycle - then you'd be looking at a finite cycle of how many people you can bring in total: basically until the entire population is working for the same MLM/Pyramid Scheme. The code below shows how quickly a pyramid scheme stops.
"""

##############################################
### Legend of variables and what they mean ###
##############################################
"""
populationOnEarth = the total population you put in
n = number of people each person has to recruit

cycle = the round of people. For instance, if you recruit 3 people, then there are 2 rounds (yourself, and the three people you recruited). If those 3 people recruit 3 people each, then that is another round (or cycle)

listLevels = the list of each round of recruits (i.e. [1, 3, 9, 27]) first person may get 3 people, those 3 people get 3 each (9), those 9 get 3 each (27), etc

levelRecruited = the current round of how many are there (round 3 in the above list would be 9 people)
"""
###########################
##### the work itself #####
###########################
query = int(input("What is the population you wish to use? "))
query2 = int(input("How many people does each person have to recruit? "))
class PyramidSchemers():
  def __init__(self, populationOnEarth=query, n=query2):
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
  
  """
  change the print line as you please: first element is depending on the population in your area (or if you wish to use the global population); second element is how many people each person must recruit
  """
  
  ################
  ### Payments ###
  ################
  
  def payment(self, pay, fee):
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
    
    for payment in self.levelPayments:
      fpayment = "{:,}".format(payment)
      self.hierarchy[f'Tier {self.levelPayments.index(payment) + 1}:'] = ("$" + fpayment)

    return self.hierarchy

pyra = PyramidSchemers()
print(pyra.payment(100, 0.30))
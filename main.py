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
                ### the function itself ###
                ###########################
def mlm(populationOnEarth, n):
  cycle = 0
  levelRecruited = 0
  listLevels = []
  
  while sum(listLevels) < populationOnEarth:
    levelRecruited = n ** cycle

    if sum(listLevels) >= populationOnEarth:
      break
    elif sum(listLevels) < populationOnEarth:
      cycle += 1
      listLevels.append(levelRecruited)

  listLevels.pop()
  total = sum(listLevels)
  total = "{:,}".format(total)
  return (f"There will be {total} people working for this MLM. The amount of rounds each person can acquire {n} people is {cycle}")

print(mlm(7000000000, 5))

"""
change the print line as you please: first element is depending on the population in your area (or if you wish to use the global population); second element is how many people each person must recruit
"""
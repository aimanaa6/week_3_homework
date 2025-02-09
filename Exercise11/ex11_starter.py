#!/usr/bin/python

# Belgium (variable) is defining a string
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# a line of hyphens same length as the Belgium string
# len is a function which requires an object which must be a sequence/collection to be placed inside
#len(Belgium) works out the length of the string stored in Belgium
# it calculates the no of characters in the string
# the makes a new string with hyphens only that is equal to the characters of the original string
print ('-' * len(Belgium))

# .replace is a method used to replace string values
# values must be positioned old then new in quote marks
# in this case it has replaced all the colons stored in the variable Belgium with semi colons
print (Belgium.replace(",",":"))


# the split method splits the string into a list
population = Belgium.split (",")
print (population)

# this helps in locating the correct values/fields
# which are required to calculate the combined population of Belgium & Brussels
# 1 in the sequence is belgium's population and 3 is brussel's population
print (population [1])
print (population [3])

# total population is defined here to calculate and print the population of Belgium & Brussels

total_population= int(population[1])+int(population[3])
print(total_population)

# total_population=int(population[1])+int(population[3])
# print(total_population)
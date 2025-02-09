#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium)
# Print a line of hyphens the same length as the string
print('-' * len(Belgium))

# Replace commas with colons and print the new version
print("String with replacement:", Belgium.replace(",", ":"))
# NOTE: strings are immutable so the original string has not changed

# Add population of belgium and brussels
data = Belgium.split(",")
# splits string into a list using a separator (commas in this case)
print(data)

# gets the population of Belgium (2nd item in the list) and converts to an integer
belgium_pop = int(data[1])

# gets the population of Brussels (4th item in the list) and converts to an integer
brussels_pop = int(data[3])

total_pop = belgium_pop + brussels_pop
print(total_pop)
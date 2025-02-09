# !/usr/bin/python
# shebang = use this program to run the file
# path to python program in computer

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium)
# Belgium variable contains a string
# print is function

print (len(Belgium))
# len is a function that prints the number of characters in a string
print('-'* 81)
# use * as the overload operator to multiply the string (-) with the number of characters (81) - integer

list_Belgium=Belgium.split(",")
# uses substrings in a string and returns a list - the comma is the seperator and it is used to split the string
# strings are immutable (cannot be changed) - turns this into a list to separate each substring
# lists are mutable, can be changed

print(list_Belgium)
print(':'.join(list_Belgium))
# concatenates any number of strings
# calling on the string (colon) to become the seperator and insert itself between each string, to make it one string.

print(list_Belgium[1])
print(list_Belgium[3])
# calling on the position in the list (Belgium and Brussels population)
# counting up from zero

Population = int(list_Belgium[1]) + int(list_Belgium[3])
print(Population)
# Convert both values from strings into integers using 'int' function
# Perform calculation to produce final value


# print('Belgium','10445852','Brussels','737966','Europe','1830','Euro','Catholicism','Dutch','French','German', sep=':')
# list_Belgium= ['Belgium','10445852','Brussels','737966','Europe','1830','Euro','Catholicism','Dutch','French','German']
# print(list_Belgium)
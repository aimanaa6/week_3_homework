#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print(Belgium)

print (len(Belgium))

print('-'* 81)

# print(Belgium, sep=':')

# separate = Belgium.split(':')
#
# print(separate)

print('Belgium','10445852','Brussels','737966','Europe','1830','Euro','Catholicism','Dutch','French','German', sep=':')

list_Belgium= ['Belgium','10445852','Brussels','737966','Europe','1830','Euro','Catholicism','Dutch','French','German']
print(list_Belgium)
print(':'.join(list_Belgium))

print(list_Belgium[1])
print(list_Belgium[3])

Calaculation = int(list_Belgium[1]) + int(list_Belgium[3])
print(Calaculation)
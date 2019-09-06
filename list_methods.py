x=[10,20,30,40,50,60]
print(x)
x.append(80)
print(x)
#####insert##############
x.insert(2,70)
print(x)
####counting a no of times a number is#####
print(x.count(40))
#####finding index#####
print(x.index(70))
########duplication###########
y=x.copy()
print(y)
###########method remove by number#########
x.remove(70)
print(x)
##########remove by indexing#########
x.pop(2)
print(x)
#####################################
z=[90,100,110]
print(z)
##############extending x by adding list of z#################
x.extend(z)
print(x)
#########sorting by default it will sort in ascending order######
x.sort()
print(x)
##########reversing################
x.reverse()
print(x)
#########clear the list##########
x.clear()
print(x)

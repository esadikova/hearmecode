#goal 1:
# bread = 3
# peanutbutter = 4
# jelly = 0

# if bread >= 2 and peanutbutter >= 1 and jelly>=1:
# 	print "You can make a PBJ sandwich"
# else:
# 	print "You cannot make a PBJ sandwich"

#goal 2:
# bread = 19
# peanutbutter = 10
# jelly = 10

# if bread >= 2 and peanutbutter >= 1 and jelly>=1:
# 	print "I can make this many sanwiches: {0}" .format(min(bread/2,peanutbutter,jelly))
# else:
# 	print "You cannot make a PBJ sandwich"

#goal 3:
# bread = 2
# peanutbutter = 5
# jelly = 1

# if bread >= 2 and peanutbutter >= 1 and jelly>=1:
# 	print "I can make this many sanwiches: {0}" .format(min(bread/2,peanutbutter,jelly))
# 	if bread%2==1 and jelly%2==1 and peanutbutter%2==1:
# 		print "You can also make an open faced sandwich"
# else:
# 	print "You cannot make a PBJ sandwich"



# #goal 4:
# bread = 5
# peanutbutter = 5
# jelly = 0

# if bread >= 2 and peanutbutter >= 1 and jelly>=1:
# 	print "I can make this many PBJ sanwiches: {0}" .format(min(bread/2,peanutbutter,jelly))
# 	if bread%2==1 and jelly%2==1 and peanutbutter%2==1:
# 		print "You can also make an open faced sandwich"
# elif jelly==0:
# 	print "You can only make a peanutbutter sandwich"
# 	print "You can make this many peanutbutter sandwiches: {0}" .format(min(bread/2,peanutbutter))
# else:
# 	print "Not included"

#goal 4.5
bread = 5
peanutbutter = 5
jelly = 3

if bread >= 2 and peanutbutter >= 1 and jelly>=1:
	numberpbj=min(bread/2,peanutbutter,jelly)
	print "I can make this many PBJ sandwiches: {0}" .format(numberpbj)
	numberpbleft = numberpbj-min(bread/2,peanutbutter)
	print "I can make this make peanutbutter sandwiches with the leftovers: {0}" .format
	if bread%2==1 and jelly%2==1 and peanutbutter%2==1:
		print "You can also make an open faced PBJ sandwich"
	if peanutbutter>jelly:
		print "You can also make {0} peanutbutter only sandwiches with the leftovers" .format(peanutbutter-jelly)
elif jelly==0:
	print "You can only make a peanutbutter sandwich"
	print "You can make this many peanutbutter sandwiches: {0}" .format(min(bread/2,peanutbutter))
else:
	print "Not included"





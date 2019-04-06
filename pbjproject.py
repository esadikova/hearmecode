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
# elif bread%2==1 and jelly%2==1 and peanutbutter%2==1:
# 		print "You can ONLY make an open faced sandwich"
# else:
# 	print "You cannot make a PBJ sandwich"

#goal 4:
bread = 2
peanutbutter = 5
jelly = 1

if bread >= 2 and peanutbutter >= 1 and jelly>=1:
	print "I can make this many sanwiches: {0}" .format(min(bread/2,peanutbutter,jelly))
	if bread%2==1 and jelly%2==1 and peanutbutter%2==1:
		print "You can also make an open faced sandwich"
elif bread%2==1 and jelly%2==1 and peanutbutter%2==1:
		print "You can ONLY make an open faced PJB sandwich"
else:
	print "You cannot make a PBJ sandwich"
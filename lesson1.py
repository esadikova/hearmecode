#print "Watch out, World!"

# twitter = "@hearmecode"

#print twitter

#print "twitter"

#contactinfo = "Eleonora Sadikova \neleonorasadikova@gmail.com \t (703)405-9723"

#print contactinfo

# lessonstring = "Lesson \t\tTopic \n1 \t\t\tStrings and Conditionals \n2 \t\t\tLists and Loops \n3 \t\t\tDictionaries & Files"

# print lessonstring

# print len(lessonstring)

# print twitter[1:]

# phone = "(202)456-7890"

# print phone[0:6]

# print phone[6:9]

# print phone[10:]

# print phone[1:4]

# print phone[0:6:2]

# name = "Eleonora"
# age = 24

# print "My name is: {0} \nMy age is: {1}" .format(name,age)

# phone = "202-555-6789"

# print "Call {0} for great pizza" .format(phone[4:])

# print "Call {0} for great pizza" .format(name)

# tweet = "In just over one year"

# print "That tweet is {0} characters. You have {1} characters left" .format(len(tweet),140-len(tweet))

# phone = "202-555-9876"

# print "Area Code: {0}" .format(phone[0:3])
# print "Local: {0}" .format(phone[4:])
# print "Different format: ({0}){1}" .format(phone[0:3],phone[4:])
# print " "
# print "Area Code: {0} \nLocal: {1} \nDifferent Format:({2}){3}" .format(phone[0:3],phone[4:],phone[0:3],phone[4:])
# print " "

# email = "shannon@hearmecode.com"
# print email.find("@")
# print email.find("z")
# -1 means not found

#print twitter.replace("@","#")

# twitter = twitter.replace("@","#")

# print twitter
# print tweet

# length = len(tweet)
# print length 

# student = 10
# capacity = 50

# if student < capacity:
# 	print "Keep recruiting"
# else: 
# 	print "End ticket signups"

volunteers = 95
goal = 100

if volunteers < goal:
	numberleft = goal-volunteers
	if numberleft <=10:
		print "So close! you need {0} more to meet the goal" .format(numberleft)
	else:
		print "Keep recruiting"
		print "You need {0} more to meet the goal" .format(numberleft)
elif volunteers == goal:
	print "You met the goal!"
elif volunteers > goal:
	print "Stop recruiting"
	print "You have recruited {0} too many" .format(volunteers-goal)
else: 
	print "not sure what is going on here"





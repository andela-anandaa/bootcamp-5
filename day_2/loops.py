# loops
names = "James Clare Brian Ann Eric Sammy".split()

count = 0
for i in range(20, 26):
    print "I'm {0}, and I'm {1} y/o".format(names[count], i)
    # print "I'm %s, and I'm %s y/o" % (name[count], i)
    count += 1

# print from 10 to zero, in one line
for i in range(10, -1, -1):
    print i,

# use a while loop
def countdown(x):
number = 10
while number >= 0:
    print number,
    number -= 1

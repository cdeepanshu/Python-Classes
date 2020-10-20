def check():
    datafile = file('example.txt')
    found = False
    for line in datafile:
        if world in line:
            found = True
            break

check()
if True:
    print "true"
else:
    print "false"

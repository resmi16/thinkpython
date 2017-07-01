filename=input('enter afile name')
for line in reversed( list(open(filename))):
    print (line.rstrip())

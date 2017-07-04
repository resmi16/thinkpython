import math
def hypotenuse(p,q):
	h1=p**2
	h2=q**2
	l=h1+h2
	hyp=math.sqrt(l)
	return hyp
x=input('Enter first side length')
y=input('Enter second side length')
print (hypotenuse(int(x),int(y)))

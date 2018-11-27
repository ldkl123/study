import numpy as np
import pylab

def func(a, b, c): 
	#@np.vectorize
	def f(x): 
		return a*x**2 + b*x + c 
	return f

if __name__=="__main__":
    file = open("../data/data.txt", "r") 

    i = 0
    for line in file: 
	    a, b, c = line.split()
	    a = float(a); b = float(b); c = float(c) 
	    print(a)
	    f = func(a, b, c)
	    ax = -b/(2*a)
	    X = np.arange(ax-4, ax+4, 0.01)

	    pylab.scatter(X, f(X), 1) 
	    pylab.ylabel(' y ')
            pylab.xlabel(' x ')
	    pylab.title('f (x)')
	    pylab.grid(True) 

    pylab.savefig('result/func1.png') 
else:
    print('Imported')

import numpy as np
import matplotlib.pyplot as plot   

def func(): 
    x = np.arange(0,2*np.pi,0.1)   
    y = np.sin(x)
    z = np.cos(x)
    plot.plot(x,y,x,z)
    plot.show()

if __name__ == "__main__":
    func()

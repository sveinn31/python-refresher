import matplotlib.pyplot as plt
import numpy as np

def func(): 
    x = np.arange(0,2*np.pi,0.1)   
    y = np.sin(x)
    z = np.cos(x)
    #plt.plot(x,y,x,z)
    #plt.show()
    t = np.arange(0.0, 1, 0.01)
    s = np.tan(t)
    plot.plot(x,y,x,z,t,s)
    plot.show()

if __name__ == "__main__":
    func()

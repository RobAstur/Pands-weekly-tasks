# For this project I used multiple websites
#https://matplotlib.org/ , https://www.geeksforgeeks.org/, https://stackoverflow.com/, https://www.w3schools.com/
#Author: Roberto Gomez Garcia

import numpy as np
import matplotlib.pyplot as plt


random_values = np.random.normal(loc = 5, scale = 2, size =1000)
plt.hist(random_values,bins=100, facecolor = 'mediumseagreen', edgecolor='slategrey', linewidth=1)
plt.title('Normal Distribution',fontsize = 13) 
plt.xlabel('frecuency', fontsize = 12) 
plt.ylabel('Values', fontsize = 12) 
plt.legend(["Dataset"])
plt.show()

axe_x = np.array(range(1,10))
axe_y = axe_x**3
plt.figure(facecolor='deepskyblue')
plt.plot(axe_x,axe_y, color = "darkorange", linestyle = "solid", linewidth = 3)
plt.title('h(x)=x3',fontsize = 14) 
plt.grid(linestyle='--', linewidth=0.5)
plt.show()
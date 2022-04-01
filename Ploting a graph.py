
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
 
# Creating vectors X and Y
# t = np.array([205,210,215,220,240,250,260,280,300,300,320,350,400,450,500])
t = np.array([5,20,50,100,150, 200, 205, 210, 215, 220, 240, 260, 320, 400, 500])
x= np.array([0,5,10,15,20,25,30,40,50,60,80,100,120,150,200,300, 500])
y = 5.357*(1-(2.178)**(-x/21.21))
z = 5.3566 * 2.178**(-t/21.21)
 
fig = plt.figure(figsize = (10, 5))
# Create the plot
plt.plot(x, y, 'g:',  label = 'Charging')
plt.plot(t, z, 'y-,',  label = 'Discharging')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
 
plt.title('Charging and discharging graph')
plt.legend()
 
# Show the plot
plt.show()


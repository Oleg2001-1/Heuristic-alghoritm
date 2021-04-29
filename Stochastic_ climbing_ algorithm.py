#Program author : Aleh Iotchanka
#Indeks number : 308908
#Language: Python
import random  
from math import e
import numpy         
import matplotlib.pyplot as pyplot  #for drawing plot

#Limits for x
x_up = 12.0
x_down = -2.0

#Standard deviation
sigma = 7   

#The investigated function
y = "5*(e**(-(x**2)/2)) + 4*(e**(-((x-9)**2)/8))"

#Stochastic climbing algorithm
def algorithm(x_up,x_down,y,sigma):
    x = random.randint(x_down,x_up)   #Choosing a work point at random
    x_for_plot = x                    #We remember the starting point for further research of its influence on the result
    x_coord = [x]                           
    for i in range(100):                    
        new_x = numpy.random.normal(x, sigma)   #Selecting neighbors of point x
        if eval(y,{'x': new_x, 'e' : e}) > eval(y,{'x' : x ,'e': e}):    #Checking if the value of the function is better with the new value of x
            if new_x < x_down or new_x > x_up:  #Checking, or the value of x does not go beyond the specified limit
                continue
            x = new_x         #x_new becomes the new work point
            x_coord.append(x)   #x is added to the list of items
    return eval(y,{'x': x_coord[len(x_coord)-1], 'e': e}), x_for_plot

itterations = 40  #Number of itterations of the algorithm

#A function, that displays the average results in the console
#and plots the dependence of the result against the position of the starting point

def output(itterations): 
    outputs = []   #List of values ​​of the objective function of the found solutions
    coordinates = []  #List of starting points
    for i in range(itterations):
        output = algorithm(x_up, x_down, y, sigma)   
        outputs.append(output[0])   #Filling the list with values of the objective function
        coordinates.append(output[1])  #Filling the list of starting points
    print('Middle value:', sum(outputs)/itterations)   #Calculates the average value of the objective function
    print('Maximal value:', max(outputs))   #Calculates the maximal value of the objective function
    print('Minimal value:', min(outputs))   #Calculates the minimal value of the objective function
    print('Standart deviation:', numpy.std(outputs)) #Calculates the root mean square (standard) deviation of the values ​​of the list outputs 
   
   #Plotting the dependence of the objective function value on the position of the starting point
    figure, ax = pyplot.subplots(1,1)
    pyplot.plot(coordinates, outputs, 'o')
    ax.set_xlabel('Start_x')
    ax.set_ylabel('y')
    ax.set_title("Dependence of the result on the position of Start_x", fontsize = 13)
    pyplot.grid(True) 
    pyplot.show()

output(itterations)














































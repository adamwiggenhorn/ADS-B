# region imports
import matplotlib.pyplot as plt
import numpy as math
from ParseCSVFile import CreateAircrafts, Aircraft
from time import sleep


# endregion

# region Functions
def PlotPlanes():
    plt.ioff()

    plt.subplot(projection='polar')

    for set in coordinatesToPlot:
        plt.scatter(set[1], set[0])
    plt.show()

def SimulatePlanes():

    for plane in aircrafts:
        for time in plane.clock:
            clockList.append(float(time))

    clockList.sort()
    timeStep = (float(clockList[len(clockList)-1]) - float(clockList[0])) / SIMULATION_TIME

    for counter in range(0, SIMULATION_TIME):
        for plane in aircrafts:
            for index in range(0, len(plane.clock)):

                if (float(plane.clock[index]) <= clockList[0] + timeStep * (counter+1)) and (float(plane.clock[index]) >= clockList[0] + timeStep * counter):

                    if planesOnPlot.__contains__(plane.ID):
                        indexOfPlane = planesOnPlot.index(plane.ID)
                        coordinatesToPlot[indexOfPlane] = [plane.radius[index], plane.angle[index]]
                    else:
                        planesOnPlot.append(plane.ID)
                        coordinatesToPlot.append([plane.radius[index], plane.angle[index]], )

        PlotPlanes()














# endregion

# Create the list of aircraft objects.
aircrafts = CreateAircrafts()

# constants
SIMULATION_TIME = 5
# variables
clockList = []
coordinatesToPlot = []
planesOnPlot = []

SimulatePlanes()

print('y')
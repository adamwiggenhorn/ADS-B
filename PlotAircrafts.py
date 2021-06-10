# region imports
import matplotlib.pyplot as plt
from ParseCSVFile import CreateAircrafts, Aircraft
from time import sleep
# endregion

# region Functions
def PlotPlaneLocations(polarCoordinates, rmax = 150):
    # Variables
    theta = []
    radius = []

    # Plot initiations
    plt.cla()
    plt.ion()
    ax = plt.subplot(projection='polar')
    ax.set_rlim(0, rmax)
    ax.set_thetagrids([0, 45, 90, 135, 180, 225, 270, 315], ['E', 'NE', 'N', 'NW', 'W', 'SW', 'S', 'SE'])
    ax.set_title('All plane locations with respect to acquisition point (mi)')

    # Adding the angle and radius values from the polarCoordinates list to two separate lists.
    # This is done for plotting purposes.
    for set in polarCoordinates:
        theta.append(set[0])
        radius.append(set[1])
        if SHOW_HEXID:
            plt.annotate(set[2], xy=(set[0], set[1]))
        elif NUMBER_PLANES:
            plt.annotate(set[3], xy=(set[0], set[1]))

    # Make a scatter plot of the angle and radius values added the the angle and radius lists above.
    # This will add every plane's position to the polar plot.
    plt.scatter(theta, radius, marker = 'x', )
    plt.pause(0.00000000001)


# **********************************************************************************************************
# This function will simulate the position of every plane in the aircrafts list.
# **********************************************************************************************************
def SimulateAllPlanes(aircrafts):

    # Variables
    clockList = []
    radiusList = []
    coordinatesToPlot = []
    planesOnPlot = []
    numberID = range(0, len(aircrafts))

    # Creates a list of the clock and radius values of every plane at every data point.
    for plane in aircrafts:
        for planeIndex in range(0,len(plane.clock)):
            clockList.append(float(plane.clock[planeIndex]))
            radiusList.append(float(plane.radius[planeIndex]))


    # Variables
    startClock = min(clockList)
    endClock = max(clockList)
    maxRadius = max(radiusList)

    # Setting the timeStep which is the variable which determines how many clock values
    # are covered in each simulation refresh.
    timeStep = (endClock - startClock) / (SIMULATION_TIME/ REFRESH_TIME)

    # This loop goes through once for every simulation refresh.
    for counter in range(0, int(SIMULATION_TIME/REFRESH_TIME)):

        # This will remove the planes that have not been updated recently from the lists
        # that are used to plot the planes.
        if REMOVE_LOST_PLANES:
            coordinatesToPlot.clear()
            planesOnPlot.clear()

        # This loop will go through every plan in the aircrafts list.
        for plane in aircrafts:

            # This loop will run once for every value held in the current planes clock list.
            # It will have an increasing index every time it runs.
            for index in range(0, len(plane.clock)):

                # If the current plane information is an update from the previous information
                # but not too far into the future (within a specified time range).
                if (float(plane.clock[index]) <= startClock + timeStep * (counter+1)) \
                        and (float(plane.clock[index]) >= startClock + timeStep * (counter-OLD_PLANE_BUFFER)):

                    # If the plot already contains this plane.
                    if planesOnPlot.__contains__(plane.ID):
                        # Find the index of this plane with respect to where it is located in the plot list.
                        indexOfPlane = planesOnPlot.index(plane.ID)

                        # Use the index fund above to update the plots information about this plane.
                        coordinatesToPlot[indexOfPlane] = \
                            [plane.angle[index], plane.radius[index], plane.ID, numberID[aircrafts.index(plane)]]

                    # If this is a new plane to the plot.
                    else:
                        # Add this plane's hexid to the list of current planes on plot.
                        planesOnPlot.append(plane.ID)

                        # Add this plane's information to the plot information.
                        coordinatesToPlot.append(
                            [plane.angle[index], plane.radius[index], plane.ID, numberID[aircrafts.index(plane)]])

        # Plot all the planes that have information in the coordinatesToPLot list.
        PlotPlaneLocations(coordinatesToPlot, maxRadius*AXIS_BUFFER_PERCENT)

        # This pauses the program so that the plot doesnt update constantly.
        sleep(REFRESH_TIME)

# endregion

# constants
REFRESH_TIME = 0.1
SIMULATION_TIME = 20
REMOVE_LOST_PLANES = False
OLD_PLANE_BUFFER = 2
AXIS_BUFFER_PERCENT = 1.1
SHOW_HEXID = False
NUMBER_PLANES = True

# Create the list of aircraft objects.
planes = CreateAircrafts()

# Simulate the plane's locations.
SimulateAllPlanes(planes)
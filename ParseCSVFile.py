# region Imports
import csv
import matplotlib.pyplot as plt
# endregion

# region Classes

# ******************************************************************************************
# This is a class representing an aircraft
# ******************************************************************************************
class Aircraft:
    def __init__(self, hexID):
        self.ID = hexID
        self.clock = []
        self.latitude = []
        self.longitude = []
        self.altitude = []
        self.speed = []
        self.indexes = []

    def FindMyIndexes(self, idList):
        for index in range(0, len(idList)):
            if idList[index] == self.ID:
                self.indexes.append(index)

    def FillInfo(self, clockList, latitudeList, longitudeList, altitudeList, speedList):

        for index in self.indexes:
            # Add the clock, latitude, longitude, altitude, and speed data for this specific aircraft
            self.clock.append(clockList[index])
            self.latitude.append(latitudeList[index])
            self.longitude.append(longitudeList[index])
            self.altitude.append(altitudeList[index])
            self.speed.append(speedList[index])

# endregion

# region Functions

# ******************************************************************************
# Opens the csv file and copies the information over to another variable that can
# be read after the file is closed
# ******************************************************************************
def OpenCSVFile(path, delimiter="\t"):
    # Initialize the variables
    retValue = []

    # Open and format the specified csv file
    newFile = open(path)
    delimitedFile = csv.reader(newFile, delimiter=delimiter)

    # Convert file into a list of the files rows
    for row in delimitedFile:
        retValue.append(row)

    # Close the file
    newFile.close()

    return retValue


# ************************************************************************************************
# Throw the lines of the csvFile that contain the required information into different lists and parses
# that data in order to get lists for hexid, speed, latitude, longitude, altitude, and clock.
# ************************************************************************************************
def ParseRowData(csvFile):

    # Loop that goes through every line of the csv data.
    for line in csvFile:

        # If the current line contains the hexid, speed, latitude, longitude, altitude, and clock
        # data it will be parsed into separate lists for the given data.
        if line.__contains__('hexid') and line.__contains__('speed') and line.__contains__(
                'position') and line.__contains__('alt') and line.__contains__('clock'):

            # Adding the parsed data into the designated lists. In addition the
            # added information that is not wanted is removed out using the split()
            # function.
            hexid.append(line[line.index('hexid') + 1])
            latitude.append(line[line.index('position') + 1].split(" ")[0])
            longitude.append(line[line.index('position') + 1].split(" ")[1])
            altitude.append(line[line.index('alt') + 1].split(" ")[0])
            clock.append(line[line.index('clock') + 1].split(" ")[0])
            speed.append(line[line.index('speed') + 1].split(" ")[0])

            # Remove the '{' at the beginning of the latitude using the replace() function.
            latitude[len(latitude) - 1] = latitude[len(latitude) - 1].replace("{", "")
# endregion

# ******************************************************************************
# This code is for parsing a specified CSV file
# ******************************************************************************

# Constants
FILE_PATH = 'C:/Users/adamw/Downloads/csvExample.csv'

# Initialize Variables
speed = []
altitude = []
clock = []
hexid = []
latitude = []
longitude = []
uniqueID = []
aircrafts = []

# Opens the csv file specified in FILE_PATH
csvFile = OpenCSVFile(FILE_PATH)

# Parses the csvFile data into separate list for clock, latitude, longitude, altitude, and speed.
ParseRowData(csvFile)


# Initiate an aircraft object for each unique aircraft in the CSV file
for id in range(0, len(hexid)):

    # If the current hexid (plane identification) is seen for the first time
    # it is added the the unique uniqueID list. There will be an Aircraft class
    # object created for each of the unique aircrafts then stored in the aircrafts list.
    if not (uniqueID.__contains__(hexid[id])):

        # adds the hexid of the current index into the uniqueID list
        uniqueID.append(hexid[id])

        # Creates and adds an object of the Aircraft class to the aircrafts list
        # with a unique hexid.
        aircrafts.append(Aircraft(hexid[id]))

# For each of the Aircraft objects created, the clock, latitude, longitude, altitude, and speed
# data of that specific aircraft are added to its object's respective lists.
for flyingThing in range(0, len(aircrafts)):

    # Finds the indexes of the current aircraft object with respect to where its information
    # is stored in the original csv data.
    aircrafts[flyingThing].FindMyIndexes(hexid)

    # Fills the data lists with the current aircraft's data found in the original csv data
    aircrafts[flyingThing].FillInfo(clock, latitude, longitude, altitude, speed)

print('h')

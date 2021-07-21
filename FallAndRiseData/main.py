import csv
import os
import math

rowData = []
maxRange = 0

def OpenDataFile(path, delimiter="\t"):
    # Initialize the variables
    retValue = []

    # Open and format the specified csv file
    newFile = open(path)
    delimitedFile = csv.reader((x.replace('\0', '') for x in newFile), delimiter=delimiter)
    #print(path)


    # Convert file into a list of the files rows
    for row in delimitedFile:
            retValue.append(row)


    # Close the file
    newFile.close()

    return retValue

aircraftDict = {710: [], 810: [], 910: [], 1010: [], 1110: [], 1210: [], 1310: [], 1410: [], 1510: [], 1610: []}
maxRange = 0

DIRECTORY = "C://ADS-B Project//aircraftDataForScript//"


for fileName in os.listdir(DIRECTORY):
    if fileName.endswith(".csv") or fileName.endswith(".txt"):
        rowData = OpenDataFile(str(DIRECTORY + fileName),',')

def calculateRange(refLat, refLong, lat, long):
    range = 2*3958.8*math.asin(math.sqrt(math.sin(math.radians(abs(refLat-lat))/2)**2+math.cos(math.radians(refLat))*math.cos(math.radians(lat))*math.sin(math.radians(abs(refLong-long))/2)**2))

    
    return range

for row in rowData:
    calculateRange(row[6], row[7])
    for key in aircraftDict:
        if float(row[3]) <= key:
            if row[4] not in aircraftDict[key]:
                aircraftDict[key].append(row[4])
            break

print(aircraftDict)




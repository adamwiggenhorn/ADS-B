import csv
import os
import math

REF_LATITUDE = 38.892711
REF_LONGITUDE = -86.849098
DIRECTORY = "/Users/jasondong/Desktop/Payload/"
rowData = []
maxRange = 0
aircraftDict = {710: [], 810: [], 910: [], 1010: [], 1110: [], 1210: [], 1310: [], 1410: [], 1510: [], 1610: []}


def OpenDataFile(path, delimiter="\t"):
    # Initialize the variables
    retValue = []

    # Open and format the specified csv file
    newFile = open(path)
    delimitedFile = csv.reader((x.replace('\0', '') for x in newFile), delimiter=delimiter)
    # print(path)

    # Convert file into a list of the files rows
    for row in delimitedFile:
        retValue.append(row)

    # Close the file
    newFile.close()

    return retValue


for fileName in os.listdir(DIRECTORY):
    if fileName.endswith(".csv") or fileName.endswith(".txt"):
        rowData = OpenDataFile(str(DIRECTORY + fileName), ',')


def calculateRange(refLat, refLong, lat, long):
    plane_range = 2 * 3958.8 * math.asin(math.sqrt(
        math.sin(math.radians(abs(refLat - lat)) / 2) ** 2 + math.cos(math.radians(refLat)) * math.cos(
            math.radians(lat)) * math.sin(math.radians(abs(refLong - long)) / 2) ** 2))

    return plane_range


for row in rowData:
    newRange = calculateRange(REF_LATITUDE, REF_LONGITUDE, float(row[6]), float(row[7]))
    if newRange > maxRange:
        maxRange = newRange
    for key in aircraftDict:
        if float(row[3]) <= key:
            if row[4] not in aircraftDict[key]:
                aircraftDict[key].append(row[4])
            break

print(aircraftDict)
for key in aircraftDict:
    print(str(key) + ": " + str(len(aircraftDict[key])))
    # print(aircraftDict[key])
print(maxRange)

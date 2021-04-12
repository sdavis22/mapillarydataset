import os
import csv

path = 'dataset/mapillary/training/images/'

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = dict()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        print("Full path: " + fullPath)
        subDir = fullPath[34:]
        print("Subdir: " + subDir)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            for _file in os.listdir(fullPath):
                allFiles[_file] = subDir
        else:
            allFiles[entry] = subDir
    return allFiles

def writeToCSV():
    fileDict = getListOfFiles(path)
    with open('dict.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in fileDict.items():
            writer.writerow([key, value])

writeToCSV()
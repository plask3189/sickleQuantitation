# sickleQuantitation with iteration over files
# Takes data from a single image and returns the percent sickle for that one image.
# Super inefficient but it works.
import os
import warnings
import openpyxl
import pandas as pds
import numpy as np

divisionList = []
#directory = os.fsencode('/Users/kateplas/Documents/Lab/ImageJproject/sickCellCountPrgrm/batchAnalysisOutput')

#os.chdir('/batchAnalysisOutput')  # Provide the new path here
os.getcwd()
directory = os.chdir('batchAnalysisOutput')
print(os.getcwd())

for file in os.listdir(directory):
    filename = os.fsdecode(file) # This method returns a string which represents the decoded filename.
    # print(filename)
    # for each csv file, get its name and run through this program. Output percentSickle in a list
    #warnings.filterwarnings("ignore")

    df = pds.read_csv(filename)

    # ----- Looks for Major and Minor columns and converts them to lists.----------
    columnMajor = df['Major']
    columnMinor = df['Minor']
    majorList = columnMajor.tolist()
    minorList = columnMinor.tolist()

    #---------- Divides the columns ---------------------------------------------

    for num1, num2 in zip(majorList, minorList):
    	divisionList.append(num1 / num2)

    # ------- For each element in divisionList, if >=2, add one to sickleCount -----
    sickleCount = 0
    for d in divisionList:
        if d >= 2:
            sickleCount = sickleCount + 1

    #------ Calculate and return percent sickle cells in the image. ------------
    percentSickle = (sickleCount / len(divisionList))*100
    print(percentSickle)

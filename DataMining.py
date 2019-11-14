#DataMining Project
import sys

#Define default variables
attributes = []
data_input = []
num_attributes = 0
num_row =0

#Function for all of the data import
def importData(file_name):
    try:
        open_file = open(file_name, "r")
    except:
        print("Couldn't find file name")
        return

        
    firstLine = open_file.readline()
    # firstLine = firstLine.translate(str.maketrans('','','<>'))
    # variable_dec = firstLine.split()
    secondLine = open_file.readline()
    secondLine = secondLine.translate(str.maketrans('','','[]'))
    global attributes 
    attributes = secondLine.split()

    global data_input
    for line in open_file:

        #Checks if a comment exists.
        if('!' in line):
            edit_line = line.split('!', 1)[0]
            line = edit_line

        editLine = line.split()
        data_input.append(editLine)


    return file_name

def MLEM2(attributes, data_input):
    return attributes






# Start of the file
print("What is the file you want to import?")
fileName = input()
importData(fileName)
print("What is the file you want to output to?")
outputFile = input()
num_attributes = len(attributes)
num_row = len(data_input)






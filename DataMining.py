#DataMining Project
import sys
# from collections import OrderedDict

#Define default variables
MLEM2_order = []
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

#Prepping the data for the input 
def data_prep(attributes, data_input, num_attributes, num_row, MLEM2_order):

    #Get Data Per Attribute
    data_per_attribute = []
    for i in range(num_attributes):
        newList = []
        for x in range(num_row):
            newList.append(data_input[x][i])
        data_per_attribute.append(newList)

    list_of_dictionaries = []
    
    for newList in data_per_attribute:
        unique = [x for i, x in enumerate(newList) if i == newList.index(x)]
        MLEM2_order.append(unique)
        unique_list = set(newList)
        #print(unique_list)
        unique_list = list(unique_list)
        dictionary_perList = {}
        for val in unique_list:
            list_of_indexes= [i for i, e in enumerate(newList) if e == val]
            dictionary_perList[val] = list_of_indexes
        
        list_of_dictionaries.append(dictionary_perList)
    #print(list_of_dictionaries)

    return list_of_dictionaries

#Perform the MLEM 2 Algo
def MLEM2(list_dic, attributes, data_input, num_attributes, num_row, MLEM2_order):

    decision = list_dic[-1]
    decision_list = MLEM2_order[-1]
    #print(decision_list)

    rules =[]
    
    # i = the decision attribute we are doing
    for i in decision_list:
        CleanMLEM2 = MLEM2_order
        elements = decision[i]
        finalList = []
        while set(elements) != set(finalList):
            similarValues = ""
            numberOfMatchingRows = 0
            
            #Goes through the list of attributes and checks
            for x in range(num_attributes-1):
                ElementList = CleanMLEM2[x]
                Dictionary_Column = list_dic[x]
                for key in ElementList:
                    dictionary_value = Dictionary_Column[key]
                    check_if_larger = list(set(dictionary_value).intersection(set(elements)))


                    #Checks if the return is empty (If so... stop considering it)
                    if not check_if_larger:
                        CleanMLEM2[x].remove(key)

                    if numberOfMatchingRows <= len(check_if_larger):


                    
                    # print(key)
                    # print(dictionary_value)
            #print(MLEM2_order)        
            break



    return




# Start of the file
print("What is the file you want to import?")
fileName = input()
importData(fileName)
print("What is the file you want to output to?")
outputFile = input()
num_attributes = len(attributes)
num_row = len(data_input)
dictionaries = data_prep(attributes, data_input, num_attributes, num_row, MLEM2_order)
finalRules = MLEM2(dictionaries, attributes, data_input, num_attributes, num_row,MLEM2_order)










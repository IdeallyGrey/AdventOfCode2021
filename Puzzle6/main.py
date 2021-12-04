numberOfOnesInThisColumn = 0
numberOfZerosInThisColumn = 0
ogr = ""
csr = ""
list = []

def importAndCleanList():
    # opens file listOfBinaryNumbers and saves each line as a list entry
    file = open("listOfBinaryNumbers", "r")
    rowToRead = 1
    while rowToRead <= 1000:
        list.append(file.readline())
        rowToRead = rowToRead + 1
    # runs through and deletes the "\n" that is after each line
    rowToRead = 0
    while rowToRead <= 999:
        x = list[rowToRead].rstrip("\n")
        list[rowToRead] = x
        rowToRead = rowToRead + 1

def remove_All_With_X_At_Y(aString, whichColumn):
    numberOfDeletions = 1
    rowToRead = 0
    while numberOfDeletions > 0:
        numberOfDeletions = 0
        while rowToRead <= len(list) - 1:
            x = str(list[rowToRead])
            x = x[whichColumn - 1:whichColumn]
            if x == aString:
                list.pop(rowToRead)
                numberOfDeletions = numberOfDeletions + 1
            else:
                pass
            rowToRead = rowToRead + 1


# finds ogr
importAndCleanList()
columnToRead = 1
exit = "no"
while exit == "no":
    rowToRead = 0
    numberOfOnesInThisColumn = 0
    numberOfZerosInThisColumn = 0
    while rowToRead <= len(list) - 1:
        x = str(list[rowToRead])
        x = x[int(columnToRead) - 1:int(columnToRead)]
        if x == "1":
            numberOfOnesInThisColumn = numberOfOnesInThisColumn + 1
        else:
            numberOfZerosInThisColumn = numberOfZerosInThisColumn + 1
        rowToRead = rowToRead + 1
    if numberOfOnesInThisColumn > numberOfZerosInThisColumn:
        remove_All_With_X_At_Y("0", columnToRead)
    elif numberOfOnesInThisColumn < numberOfZerosInThisColumn:
        remove_All_With_X_At_Y("1", columnToRead)
    else:
        remove_All_With_X_At_Y("0", columnToRead)
    if columnToRead > 12:
        columnToRead = 1
    else:
        columnToRead = columnToRead + 1
    #print("")
    #print(list)
    if len(list) <= 1:
        exit = "yes"
ogr = list[0]

# finds csr
importAndCleanList()
columnToRead = 1
exit = "no"
while exit == "no":
    rowToRead = 0
    numberOfOnesInThisColumn = 0
    numberOfZerosInThisColumn = 0
    while rowToRead <= len(list) - 1:
        x = str(list[rowToRead])
        x = x[int(columnToRead) - 1:int(columnToRead)]
        if x == "1":
            numberOfOnesInThisColumn = numberOfOnesInThisColumn + 1
        else:
            numberOfZerosInThisColumn = numberOfZerosInThisColumn + 1
        rowToRead = rowToRead + 1
    if numberOfOnesInThisColumn < numberOfZerosInThisColumn:
        remove_All_With_X_At_Y("0", columnToRead)
    elif numberOfOnesInThisColumn > numberOfZerosInThisColumn:
        remove_All_With_X_At_Y("1", columnToRead)
    else:
        remove_All_With_X_At_Y("1", columnToRead)
    if columnToRead > 12:
        columnToRead = 1
    else:
        columnToRead = columnToRead + 1
        #print("")
        #print(list)
    if len(list) <= 1:
        exit = "yes"
csr = list[0]



# prints output
print("ogr rate: " + ogr)
print("csr rate: " + csr)

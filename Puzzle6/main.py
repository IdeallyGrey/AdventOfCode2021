numberOfOnes = 0
numberOfZeros = 0
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

def removeAllStartingWith(aString):
    rowToRead = 0
    while rowToRead <= len(list) - 1:
        x = str(list[rowToRead])
        x = x[0:1]
        if x == aString:
            list.pop(rowToRead)
        else:
            pass
        rowToRead = rowToRead + 1

# finds ogr
importAndCleanList()
lineToRead = 1
exit = 1
while exit == 1:
    rowToRead = 0
    numberOfOnes = 0
    numberOfZeros = 0
    while rowToRead <= len(list) - 1:
        x = str(list[rowToRead])
        x = x[int(lineToRead) - 1:int(lineToRead)]
        if x == "1":
            numberOfOnes = numberOfOnes + 1
        else:
            numberOfZeros = numberOfZeros + 1
        rowToRead = rowToRead + 1
    if numberOfOnes > numberOfZeros:
        removeAllStartingWith("0")
    elif numberOfOnes < numberOfZeros:
        removeAllStartingWith("1")
    else:
        removeAllStartingWith("0")
    if lineToRead > 12:
        lineToRead = 1
    else:
        lineToRead = lineToRead + 1
    print(len(list))
    if len(list) <= 1:
        exit = 0
ogr = list[0]

# finds csr
importAndCleanList()
lineToRead = 1
exit = 1
while exit == 1:
    rowToRead = 0
    numberOfOnes = 0
    numberOfZeros = 0
    while rowToRead <= len(list) - 1:
        x = str(list[rowToRead])
        x = x[int(lineToRead) - 1:int(lineToRead)]
        if x == "1":
            numberOfOnes = numberOfOnes + 1
        else:
            numberOfZeros = numberOfZeros + 1
        rowToRead = rowToRead + 1
    if numberOfOnes < numberOfZeros:
        removeAllStartingWith("0")
    elif numberOfOnes > numberOfZeros:
        removeAllStartingWith("1")
    else:
        removeAllStartingWith("1")
    if lineToRead > 12:
        lineToRead = 1
    else:
        lineToRead = lineToRead + 1
    print (len(list))
    if len(list) <= 1:
        exit = 0
csr = list[0]



# prints output
print(list)
print("ogr rate: " + ogr)
print("csr rate: " + csr)

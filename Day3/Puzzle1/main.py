numberOfOnes = 0
numberOfZeros = 0
gammaRate = ""
epsillonRate = ""

list = []

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

# does the actual counting

lineToRead = 1
while lineToRead <= 12:
    rowToRead = 0
    numberOfOnes = 0
    numberOfZeros = 0
    while rowToRead <= 999:
        x = str(list[rowToRead])
        x = x[int(lineToRead) - 1:int(lineToRead)]
        if x == "1":
            numberOfOnes = numberOfOnes + 1
        else:
            numberOfZeros = numberOfZeros + 1

        rowToRead = rowToRead + 1
    if numberOfOnes > numberOfZeros:
        gammaRate = gammaRate + "1"
        epsillonRate = epsillonRate + "0"
    else:
        gammaRate = gammaRate + "0"
        epsillonRate = epsillonRate + "1"
    lineToRead = lineToRead + 1
#3985686

# prints output
print(list)
print("Gamma rate: " + gammaRate)
print("Epsillon rate: " + epsillonRate)
print("Total:")
print(int(gammaRate) * int(epsillonRate))

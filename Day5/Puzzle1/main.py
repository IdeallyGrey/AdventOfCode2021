numberOfOnes = 0
numberOfZeros = 0
gammaRate = ""
epsillonRate = ""

list = []

# opens file listOfBinaryNumbers and saves each line as a list entry
file = open("listOfCords", "r")
rowToRead = 1
while rowToRead <= 500:
    list.append(file.readline())
    rowToRead = rowToRead + 1

# runs through and deletes the "\n" that is after each line
rowToRead = 0
while rowToRead <= 499:
    x = list[rowToRead].rstrip("\n")
    list[rowToRead] = x
    rowToRead = rowToRead + 1

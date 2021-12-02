total = 0
list = []

#opens file instructions and saves each line as a list entry
file = open("instructions", "r")
lineToRead = 1
while lineToRead <= 2000:
    list.append(file.readline())
    lineToRead = lineToRead + 1

#runs through and deletes the "\n" that is after each line
lineToRead = 0
while lineToRead <= 1999:
    x = list[lineToRead].rstrip("\n")
    x = int(x)
    list[lineToRead] = x
    lineToRead = lineToRead + 1

#does the actual counting
lineToRead = 1
while lineToRead <= 1999:
    current = list[lineToRead]
    past = list[lineToRead - 1]
    if current > past:
        total = total + 1
    lineToRead = lineToRead + 1

#prints total
print("\n\nIncreased:")
print(total)

depth = 0
distance = 0
list = []

#opens file instructions and saves each line as a list entry
file = open("instructions", "r")
lineToRead = 1
while lineToRead <= 1000:
    list.append(file.readline())
    lineToRead = lineToRead + 1

#runs through and deletes the "\n" that is after each line
lineToRead = 0
while lineToRead <= 999:
    x = list[lineToRead].rstrip("\n")
    x = str(x)
    list[lineToRead] = x
    lineToRead = lineToRead + 1

#does the actual counting
lineToRead = 0
while lineToRead <= 999:
    if 'forward' in list[lineToRead]:
        x = list[lineToRead].strip("\nforward")
        x = int(x)
        distance = distance + x
    if 'up' in list[lineToRead]:
        x = list[lineToRead].strip("\nup")
        x = int(x)
        depth = depth - x
    if 'down' in list[lineToRead]:
        x = list[lineToRead].strip("\ndown")
        x = int(x)
        depth = depth + x

    lineToRead = lineToRead + 1

#prints total
print("\n\nDepth:")
print(depth)
print("Distance:")
print(distance)
print("Total:")
print(depth * distance)

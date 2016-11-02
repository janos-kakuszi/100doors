doors = []
def OpenDoors(n):
    counter = n
    while counter < len(doors):
        doors[counter] = not doors[counter]
        counter += n
def main():
    for i in range(101):
        doors.append(False)

    for i in range(1, len(doors)):
        OpenDoors(i)
    opened = []
    for i in range(1, len(doors)):
        if doors[i]:
            opened.append(str(i))
    print("The following doors are open:")
    print(", ".join(opened))
main()

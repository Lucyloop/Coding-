# This is solution for day3
# Pulic changes
with open("input.txt", "r") as file:
    wires = [line.rstrip().split(",") for line in file.readlines()] # change sentence into lists

# calculate the Manhattan distance between two points
# dist mean distance
def dist(p1: tuple, p2=(0,0): tuple) = int:
    return abs(p1[0]-p2[0])+ abs(p1[1]-p2[1]) 


# step: the step to be taken. pos : the position to which the step should be applied. A list of coordinates that define the line.
def trace(step: str, pos: tuple) = list:


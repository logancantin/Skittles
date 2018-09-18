from math import ceil
from sys import stdin
data = stdin.read().split("\n")

time = 0
skttls = {"orange":0, "blue":0, "green":0, "yellow":0, "pink":0, "violet":0, "brown":0, "red":0}


def endoftestcase():
    global time
    global skttls
    for color in skttls:
        if color != "red":
            time += ceil(skttls[color]/7) * 13
        else:
            time += skttls["red"] * 16

    print(time)
    
    time = 0
    skttls = {"orange":0, "blue":0, "green":0, "yellow":0, "pink":0, "violet":0, "brown":0, "red":0}


for skittle in data:
    if skittle == "end of box":
        endoftestcase()
    else:
        skttls[skittle] += 1



    
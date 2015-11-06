import os

def loadData(filename):
    with open(filename, "r") as fobj:
        lines = fobj.read().split("\r")
        headers = [field.strip() for field in lines[0].split(",")]
        players = [ {
                stat.strip(): value.strip() for (stat, value) 
                    in zip(headers, line.split(","))
            }
            for line in lines[1:]
        ]

    positions = {}
    for player in players:
        if "Position" not in player:
            continue
        poslist = player["Position"].split("/")
        for pos in poslist:
            if pos not in positions:
                positions[pos] = []
            positions[pos] += [ player ]

    return positions


def printFields(fields, msgWidth=100):
    fieldWidth = msgWidth / len(fields)
    frmt = " %-" + str(fieldWidth - 1) + "s"
    print "|" + "|".join([frmt % field for field in fields]) + "|"

def printSeparator(fieldLen, msgWidth=100):
    fieldWidth = msgWidth / fieldLen
    print "|" + "|".join(["-" * fieldWidth] * fieldLen) + "|"

def printPositions(positions):
    printFields(["Position", "# Players", "Total Exp. fWAR"])
    printSeparator(3)
    for position in positions:
        matchCount = len(positions[position])
        wars = [float(player["Exp. 2016 fWAR"]) for player in positions[position]]
        totalWar = sum(wars)
        printFields([position, matchCount, totalWar])
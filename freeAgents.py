import time
import dataLoader
from itertools import combinations

positions = dataLoader.loadData("CrowdsourcingResults.csv")

dataLoader.printPositions(positions)
print ""
print ""

bold = lambda val: ("*" + str(val) + "*")

def getHighestKey(positions, pos, key, usedPlayers=[]):
	bestPlayer = None
	def doBest(pos, bestPlayer=None):
		for player in positions[pos]:
			if player in usedPlayers:
				continue
			elif bestPlayer == None:
				bestPlayer = player
			else:
				if player[key] > bestPlayer[key]:
					bestPlayer = player
		return bestPlayer

	if pos == "DH":
		# Any player can be a DH
		for position in positions:
			if position != "P":
				bestPlayer = doBest(position, bestPlayer)
	else:
		bestPlayer = doBest(pos)

	return bestPlayer

dataLoader.printFields(["Positions", "Player", "Exp. 2016 fWAR", "Exp. Salary"])
dataLoader.printSeparator(4)
totalWar = 0
totalSalary = 0
usedPlayers = []
positionOrder = ["CF", "LF", "RF", "1B", "2B", "3B", "SS", "C", "P", "P", "P", "P", "P"]
for pos in positionOrder:
	bestPlayer = getHighestKey(positions, pos, "Exp. 2016 fWAR", usedPlayers)
	dataLoader.printFields([pos, bestPlayer["Player"], bestPlayer["Exp. 2016 fWAR"], bestPlayer["Expected 2016 AAV"]])
	if bestPlayer != None:
		usedPlayers += [ bestPlayer ]
		totalWar += float(bestPlayer["Exp. 2016 fWAR"])
		totalSalary += float(bestPlayer["Expected 2016 AAV"])

dataLoader.printFields([bold("Total"), "", bold(totalWar), bold(totalSalary)])
print ""
print ""


dataLoader.printFields(["Positions", "Player", "Exp. 2016 fWAR", "Exp. Salary", "Exp. Wins/$"])
dataLoader.printSeparator(5)
totalWar = 0
totalSalary = 0
usedPlayers = []
for pos in positionOrder:
	bestPlayer = getHighestKey(positions, pos, "Expected Wins/$", usedPlayers)
	dataLoader.printFields([pos, bestPlayer["Player"], bestPlayer["Exp. 2016 fWAR"],
		bestPlayer["Expected 2016 AAV"], bestPlayer["Expected Wins/$"]])
	if bestPlayer != None:
		usedPlayers += [ bestPlayer ]
		totalWar += float(bestPlayer["Exp. 2016 fWAR"])
		totalSalary += float(bestPlayer["Expected 2016 AAV"])
dataLoader.printFields([bold("Total"), "", bold(totalWar), bold(totalSalary), bold(totalWar / totalSalary)])
print ""
print ""
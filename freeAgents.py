import time
import dataLoader

positions = dataLoader.loadData("CrowdsourcingResults.csv")

dataLoader.printPositions(positions)
print ""
print ""

def getHighestWar(positions, pos, usedPlayers=[]):
	bestPlayer = None
	def doBest(pos, bestPlayer=None):
		for player in positions[pos]:
			if player in usedPlayers:
				continue
			elif bestPlayer == None:
				bestPlayer = player
			else:
				if player["Exp. 2016 fWAR"] > bestPlayer["Exp. 2016 fWAR"]:
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
dataLoader.printSeparator()
totalWar = 0
totalSalary = 0
usedPlayers = []
positionOrder = ["CF", "LF", "RF", "1B", "2B", "3B", "SS", "C", "P", "P", "P", "DH"]
for pos in positionOrder:
	bestPlayer = getHighestWar(positions, pos, usedPlayers)
	dataLoader.printFields([pos, bestPlayer["Player"], bestPlayer["Exp. 2016 fWAR"], bestPlayer["Expected 2016 AAV"]])
	if bestPlayer != None:
		usedPlayers += [ bestPlayer ]
		totalWar += float(bestPlayer["Exp. 2016 fWAR"])
		totalSalary += float(bestPlayer["Expected 2016 AAV"])

dataLoader.printSeparator()
dataLoader.printFields(["Total", "", totalWar, totalSalary])

# def forEachPosition(keyList=[pos for pos in positions]):
# 	for player in positions[keyList[0]]:
# 		if len(keyList) == 1:
# 			yield [player]
# 		else:
# 			for combo in forEachPosition(keyList[1:]):
# 				if player in combo:
# 					continue
# 				else:
# 					yield [ player ] + combo

# posNames = [pos for pos in positions]
# comboLens = [len(positions[pos]) for pos in positions]
# comboLen = reduce(lambda x,y: x*y, comboLens)
# print "# of Combinations:", comboLen

# lastCount = 0
# curCount = 0
# startTime = 0
# def updateProg():
# 	global curCount, lastCount, startTime
# 	curCount += 1
# 	if startTime == 0:
# 		startTime = time.clock()
# 	if float(curCount - lastCount) / float(comboLen) > .001:
# 		lastCount = curCount
# 		percent = float(lastCount) / float(comboLen)
# 		now = time.clock()
# 		timeLeft = ((1.0 - percent) * (now - startTime) / percent)
# 		print "%.4f %% : ~ %5.2f seconds left" % (percent * 100.0, timeLeft)

# for combo in forEachPosition():
# 	updateProg()


import time

with open("CrowdsourcingResults.csv", "r") as fobj:
	lines = fobj.read().split("\r")
	headers = [field.strip() for field in lines[0].split(",")]
	players = [	{
			stat.strip(): value.strip() for (stat, value) 
				in zip(headers, line.split(","))
		}
		for line in lines[1:]
	]

positions = {}
for player in players:
	poslist = player["Position"].split("/")
	for pos in poslist:
		if pos not in positions:
			positions[pos] = []
		positions[pos] += [ player ]

def printFields(fields, msgWidth=80):
	fieldWidth = msgWidth / len(fields)
	frmt = " %-" + str(fieldWidth - 1) + "s"
	print "|".join([frmt % field for field in fields])

def printSeparator(msgWidth=80):
	print "-" * msgWidth

printFields(["Position", "# Players", "Total fWAR"])
printSeparator()
for position in positions:
	matchCount = len(positions[position])
	wars = [float(player["2015 fWAR"]) for player in positions[position]]
	totalWar = sum(wars)
	printFields([position, matchCount, totalWar])
print ""

def forEachPosition(keyList=[pos for pos in positions]):
	for player in positions[keyList[0]]:
		if len(keyList) == 1:
			yield [player]
		else:
			for combo in forEachPosition(keyList[1:]):
				if player in combo:
					continue
				else:
					yield [ player ] + combo

posNames = [pos for pos in positions]
comboLens = [len(positions[pos]) for pos in positions]
comboLen = reduce(lambda x,y: x*y, comboLens)
print "# of Combinations:", comboLen

lastCount = 0
curCount = 0
startTime = 0
def updateProg():
	global curCount, lastCount, startTime
	curCount += 1
	if startTime == 0:
		startTime = time.clock()
	if float(curCount - lastCount) / float(comboLen) > .001:
		lastCount = curCount
		percent = float(lastCount) / float(comboLen)
		now = time.clock()
		timeLeft = ((1.0 - percent) * (now - startTime) / percent)
		print "%.4f %% : ~ %5.2f seconds left" % (percent * 100.0, timeLeft)

for combo in forEachPosition():
	updateProg()


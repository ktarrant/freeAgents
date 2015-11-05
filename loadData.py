
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
        poslist = player["Position"].split("/")
        for pos in poslist:
            if pos not in positions:
                positions[pos] = []
            positions[pos] += [ player ]

    return positions
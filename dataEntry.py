#!/usr/bin/env python
import sys

def sortStringList(aList):
    newList = []
    for item in aList:
        try:
            newList.append(int(item))
        except ValueError:
            print 'ERROR: Skipped', item
    newList.sort()
    
    stringList = []
    for item in newList:
        stringList.append(str(item))
    return stringList
    
spaceList = {}
space = "1"
while space.lower() != "q":
    space = raw_input("Space:")
    if space.lower() == "q":
        break
    else:
        destinations = {}
        dest = "1"
        while dest.lower != 'q':
            dest = raw_input("destinaton from "+space+' ('+' '.join(destinations.keys())+'): ')
            if dest.lower() == "q":
                break
            else:
                modeList = []
                modes = raw_input(space+'->'+dest+" modes(t,b,u,(o)mit): ")
                modes = modes.lower()
                if 't' in modes:
                    modeList.append('SYTAXI')
                if 'b' in modes:
                    modeList.append('SYBUS')
                if 'u' in modes:
                    modeList.append('SYUNDERGROUND')
                modeList.append('SYBLACK')
                if not 'o' in modes.lower():
                    destinations[dest] = modeList
                else:
                    print "Ignoring destination:", dest
        spaceList[space] = destinations
allSpaces = spaceList.keys()
allSpaces = sortStringList(allSpaces)
#print allSpaces
#print spaceList
outPath = '/Users/eric/board.txt'
outFile = open(outPath, 'w')
for spaceNum in range(len(allSpaces)):
    spaceKey = allSpaces[spaceNum]
    space = spaceList[spaceKey]
    outFile.write('self.gameBoard['+spaceKey+'] =    {')
    routeList = space.keys()
    routeList = sortStringList(routeList)
    for routeNum in range(len(routeList)):
        routeKey = routeList[routeNum]
        route = space[routeKey]
        outFile.write(routeKey+': [')
        for ticketNum in range(len(route)):
            ticket = route[ticketNum]
            outFile.write(ticket) 
            
            isLastTicket = ticketNum == len(route)-1
            isLastRoute = routeNum == len(routeList)-1
            if isLastTicket and isLastRoute:
                outFile.write(']}\n')
            elif not isLastTicket and isLastRoute:
                outFile.write(', ')
            elif isLastTicket and not isLastRoute:
                outFile.write('],\n'+6*'\t')
            else:
                outFile.write(', ')
    #outFile.write('}\n')
if outFile != sys.stdout:
    outFile.close()

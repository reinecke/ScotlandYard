#
#  SYGameBoard.py
#  
#
#  Created by Eric Reinecke on 7/9/09.
#  Copyright (c) 2009 Eric Reinecke. All rights reserved.
#
# TODO: Scrap most this, use pattern.graph to express board
#       (http://www.clips.ua.ac.be/pages/pattern-graph)
# TODO: No * imports!
from SYPlayer import *
# TODO: the board should be loaded from something like yaml
import defaultBoard

# TODO: Y u no use sets!?!
def extendUniq(list1, list2):
    '''Combines list1 with list 2 ommiting repeat items'''
    newList = list1[:]
    for item in list2:
        if item not in newList:
            newList.append(item)
    
    return newList

class SYGameBoard(object):
    # TODO: list as a default value? NO!
    # TODO: No magic hard-coded stuff! Use a constant!
    def __init__(self, 
            detectiveNames=['Red', 'Purple', 'Blue', 'Green', 'Yellow'],
            mrXName = 'Mr. X'):
        '''A Game Board object'''
        
        # Build the board data
        self.gameBoard = defaultBoard.board()
                        
        # Build the starting location card stack
        # TODO: This data should be provided by the game board,
        #       there are specific locations to use
        self.startLocations = range(1,11)
        
        # Build the players
        self.players = [SYPlayer(mrXName, SYMRX)]
        for player in detectiveNames:
            self.players.append(SYPlayer(player, SYDETECTIVE))

    def checkBoardIntegrity(self):
        '''Checks game board data integrity, reports errors'''
        # TODO: This shouldn't print, it sould return a list of issues
        for node in self.gameBoard:
            nodeData = self.gameBoard[node]
            for dest in nodeData:
                # Check each node to make sure the nodes it connects to
                # connect back to it the same way
                try:
                    destNode = self.gameBoard[dest]
                except KeyError:
                    print 'ERROR: Node', dest, "linked from", node, "doesn't exist"
                    break
                try:
                    destTokens = destNode[node]
                except KeyError:
                    print 'ERROR: Node', dest, "linked from", node, "doesn't link back"
                    break
                    
                tokens = nodeData[dest]
                allTokens = extendUniq(tokens, destTokens)
                for token in allTokens:
                    if token not in tokens:
                        print 'one way', token, 'link from', dest, 'to', node
                    if token not in destTokens:
                        print 'one way', token, 'link from', node, 'to', dest
        print '--= INTEGRITY CHECK DONE =--'

    def playerAt(self, loc):
        '''Returns the SYPlayer object at a given location
        Returns None if no players are there'''
        # TODO: this should really handle multiple players at a spot
        # Check each player to see if they are at the location
        returnPlayer = None
        for player in self.players:
            if player.location == loc:
                # TODO: shouldn't this just return?
                returnPlayer = player
        
        return returnPlayer
    
    def checkMove(self, loc1, loc2, token):
        ''' Returns whether this is a legal move or not'''
        # Get loc 1
        try:
            possibleMoves = self.gameBoard[loc1]
        except KeyError:
            # Could not find loc1
            return SYNOTCONNECTED
        
        try:
            requiredTokens = possibleMoves[loc2]
        except KeyError:
            # loc2 not accessible from loc1
            return SYNOTCONNECTED
            
        if token in requiredTokens and not self.playerAt(loc2):
            return SYLEGALMOVE
        
        return SYINSUFFICENTTOKEN
    
    def movePlayer(self, player, dest, token, moveModifiers=[]):
        '''Moves player to destination using token. Returns
        the move status'''
        # First check if the move is possible
        playerLoc = player.location
        moveCheck = self.checkMove(playerLoc, dest, token)
        if moveCheck == SYLEGALMOVE and player.tokens[token] > 0:
            # Valid move, do it
            # TODO: Should the board really be doing the token accounting?
            player.tokens[token] = player.tokens[token] - 1
            player.location = dest
            player.moves.append((dest, token, moveModifiers))
            
        return moveCheck
    
    def possibleMoves(self, player=None, loc=None, tokens=None):
        '''Returns a dict of location possible to move to
        and tickets that could be used'''
        # If player is specified, get it's parameters
        if player:
            if loc is None:
                loc = player.location
            if tokens is None:
                tokens = player.tokens
        
        # Get all the possible moves for the location
        try:
            allMoves = self.gameBoard[loc]
        except KeyError:
            print "no location:", loc
            allMoves = []
       
        # TODO: Move this stuff left, why so much indent!?!
        legalMoves = {}
        # Check legality given the player's tokens
        for loc in allMoves:
            # Make sure no one is at the loc
            # But allow self at loc
            playerAtLoc = self.playerAt(loc)
            if not playerAtLoc or playerAtLoc == player:
                # Get the possible tokens that can be used to get to loc
                possibleTokens = allMoves[loc]
                
                # Validate that user has an available token
                for token in possibleTokens:
                    try:
                        numTokens = tokens[token]
                        # If there are enough tokens add this to possible moves
                        if numTokens > 0 and legalMoves.has_key(loc):
                            legalMoves[loc].append(token)
                        elif numTokens > 0:
                            legalMoves[loc] = [token]
                    except KeyError:
                        pass
                        
        return legalMoves
    
    
    def possibleLocation(self, numMoves, player=None, loc=None, tokens=None):
        '''Returns all the posible locations that could be reached
        given the parameters'''
        print "possibleLocation(self, %s, %s, %s, %s)"%(numMoves, player, loc, tokens)
        # We want other stuff to override player info for recursion
        if player:
            loc=player.location
            if not tokens:
                tokens=player.tokens
            
        # Handle different forms of tokens input
        remainingTokens = None
        # TODO: NO EXPLICIT TYPE CHECKING!!
        if type(tokens) == list:
            numMoves = len(tokens)
            tokens = tokens[0]
            remainingTokens = tokens[1:]
        
        # Get the possible Moves
        possMoves = self.possibleMoves(loc=loc, tokens=tokens)
        
        possibleLocs = possMoves.keys()
        print 'poss locs:', possibleLocs
        # TODO: MOVE LEFT!!!!!!
        # Calculate out further possible moves if we need to
        if numMoves > 1:
            possibleLocs = []
            # For each location we could go to
            for dest in possMoves:
                # for each token we could use to get to that location
                for token in possMoves[dest]:
                    print '---testing:',token
                    if not remainingTokens:
                        # using the token suppy instead of token history
                        # need to pass tokens as a copy with the 
                        remainingTokens = tokens.copy()
                        remainingTokens[token] = remainingTokens[token] -1
                    newPossibleLocs = self.possibleLocation(numMoves-1, player, dest, remainingTokens)
                    possibleLocs = extendUniq(possibleLocs, newPossibleLocs)
        return possibleLocs

# TODO: Even if tests, dump this stuff into a function, please!
board = SYGameBoard()
board.checkBoardIntegrity()
mrX=board.players[0]
mrX.tokens = {SYUNDERGROUND:1, SYBUS:1, SYTAXI:0, SYBLACK:0}
mrX.location = 1
possMoves= board.possibleMoves(mrX)
print 'possible moves', possMoves
print 'Locs:', board.possibleLocation(2, mrX)
firstMove = possMoves[possMoves.keys()[0]]
print "move:", possMoves.keys()[0], firstMove[0]
print board.movePlayer(mrX, possMoves.keys()[0], firstMove[0])
print board.possibleMoves(mrX)
print mrX.moves

            

#
#  SYPlayer.py
#  
#
#  Created by Eric Reinecke on 7/9/09.
#  Copyright (c) 2009 SAN Productions. All rights reserved.
#

# Ticket declarations
SYTAXI = 'Taxi'
SYBUS = 'Bus'
SYUNDERGROUND = 'Underground'
SYBLACK = 'Black'
SY2X = '2X'
SYSTARTTOKEN = 'StartToken'

# Team Constants
SYMRX = 'Mr.X'
SYDETECTIVE = 'Dectective'
SYPSUEDOPLAYER = 'PsuedoPlayer'

# Move Constants
SYLEGALMOVE = 'LegalMove'
SYPLAYERATDEST = 'PlayerAtDestinaton'
SYINSUFFICENTTOKEN = 'InsufficentToken'
SYNOTCONNECTED = 'NotConnected'


class SYPlayer(object):
    def __init__(self, name, team):
        # Set up starting tokens
        if team == SYDETECTIVE:
            self.tokens = {SYTAXI: 10,
                            SYBUS: 8,
                            SYUNDERGROUND: 4}
        elif team == SYMRX:
            self.tokens = {SYTAXI: 4,
                            SYBUS: 3,
                            SYUNDERGROUND: 3,
                            SYBLACK: 5,
                            SY2X: 2}
        
        # Set up location, 0 is nowhere
        self.location = 0
        
        # Set up the move log
        self.moves = []

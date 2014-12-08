###
# Copyright (c) 2014, clrh
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import csv
import pprint

class TeamMeteo(callbacks.Plugin):
    """Add the help for "@plugin help TeamMeteo" here
    This should describe *how* to use this plugin."""
    pass

    metrics = {}

    def __init__(self, irc):
        self.__parent = super(TeamMeteo, self)
        self.__parent.__init__(irc)

    def bmeteo(self,irc,msg,args):
        """takes no arguments

        Displays some data
        """
        irc.reply(str('coucou'))

    def _loadmetrics(self):
        with open ('mock2.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                self.metrics[row[0]] = row[1]

    def getnbhl(self,irc,msg,args):
        self._loadmetrics
        print "pouet"
        print self.metrics
        irc.reply(str(self.metrics['demandes HL']))

Class = TeamMeteo


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:

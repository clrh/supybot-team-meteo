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
#import wget

class TeamMeteo(callbacks.Plugin):
    """Add the help for "@plugin help TeamMeteo" here
    This should describe *how* to use this plugin."""
    pass

    metric_file = 'mock2.csv'
    metrics = {}

    def __init__(self, irc):
        self.__parent = super(TeamMeteo, self)
        self.__parent.__init__(irc)

    def bmeteo(self,irc,msg,args):
        """takes no arguments

        Displays some data
        """
        irc.reply(str('coucou'))

#    def _getnewfile(self):
#        url = 'https://docs.google.com/spreadsheets/d/1B_0sZ74_jrFZo1GbyGmUQe2CJ5gklevunvt5EFxUA7g/export?format=csv&gid=1272107489&single=true'
#        filename = wget.download(url)
#        print filename

    def _loadmetrics(self):
        with open (self.metric_file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                self.metrics[row[0]] = row[1]

    def getnbhl(self,irc,msg,args):
        self._loadmetrics()
        print self.metrics
        irc.reply(str(self.metrics['demandes HL']))

Class = TeamMeteo


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:

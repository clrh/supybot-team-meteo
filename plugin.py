#!/usr/bin/python
# -*- coding: utf-8 -*-

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import csv
import urllib

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

    def _getnewfile(self):
        """download the fresh csv file"""
        url = 'https://docs.google.com/spreadsheets/d/1B_0sZ74_jrFZo1GbyGmUQe2CJ5gklevunvt5EFxUA7g/export?format=csv&gid=1272107489&single=true'
        file = urllib.URLopener()
        self.metric_file = "metrics.csv"
        file.retrieve(url,self.metric_file)

    def _loadmetrics(self):
        """load metrics from the csv file in memory"""
        with open (self.metric_file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                self.metrics[row[0]] = row[1]

    def hlstat(self,irc,msg,args):
        self._loadmetrics()
        s = self.metrics
        statustxt = s['demandes HL'] + " en HL: "
        if s['48h'] != '':
            statustxt += s['48h'] + " 48h, "
        if s['urgent'] != '':
            statustxt += s['urgent'] + " urgent(s), "
        if s['haut'] != '':
            statustxt += s['haut'] + " haut(s)" 
        irc.reply(str(statustxt))

    def devstat(self,irc,msg,args):
        """give me the status of developpment sprint"""
        self._loadmetrics()
        s = self.metrics
        statustxt = s['points engagés'] + " points engagés dont " \
                + s['points bonus'] + " points bonus, " \
                + s['points terminés'] + " points terminés de " \
                + s['stories terminées'] + " stories"
        irc.reply(str(statustxt))

    def wtdn(self,irc,msg,args):
        """what to do now ?"""
        self._loadmetrics()
        s = self.metrics
        statustxt = ''
        if s['à intégrer'] != '':
            statustxt += s['à intégrer'] + " à intégrer, "
        if s['à tester'] != '':
            statustxt += s['à tester'] + " à tester, "
        if s['à rt'] != '':
            statustxt += s['à rt'] + " à rt, " 
        if s['à documenter'] != '':
            statustxt += s['à documenter'] + " à documenter" 
        irc.reply(str(statustxt))

    def testdata(self,irc,msg,args):
        self._getnewfile()
        self._loadmetrics()
        irc.reply(str('test'))

Class = TeamMeteo


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:

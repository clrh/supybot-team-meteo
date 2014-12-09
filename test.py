#!/usr/bin/python
# -*- coding: utf-8 -*-
###
# Copyright (c) 2014, clrh
# All rights reserved.
#
#
###

from supybot.test import *

class TeamMeteoTestCase(PluginTestCase):
    plugins = ('TeamMeteo',)

    def testTeamMeteo(self):
        self.assertNotError('bmeteo')
        self.assertResponse('bmeteo','coucou')
    
    def testGetMetrics(self):
        self.assertResponse('hlstat','46 en HL: 2 urgent(s), 7 haut(s)')
        self.assertResponse('devstat','14 points engagés dont 0 points bonus, 3 points terminés de 2 stories')

    def testWhatToDoNow(self):
        self.assertResponse('wtdn','3 à intégrer, 1 à tester, 2 à rt, 1 à documenter')

    def testdata(self):
        self.assertResponse('testdata','test')

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

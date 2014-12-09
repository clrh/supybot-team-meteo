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
        self.assertResponse('hlstatus','46 en HL: 2 urgent(s), 7 haut(s)')
        

    def testdata(self):
        self.assertResponse('testdata','test')

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

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
        self.assertResponse('getnbhl','46')

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

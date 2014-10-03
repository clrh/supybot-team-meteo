###
# Copyright (c) 2014, clrh
# All rights reserved.
#
#
###

from supybot.test import *

class TeamMeteoTestCase(PluginTestCase):
    plugins = ('TeamMeteo',)


    def testDuTest(self):
        self.assertResponse('pouet','zut')

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

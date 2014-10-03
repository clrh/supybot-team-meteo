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

class TeamMeteo(callbacks.Plugin):
    """Add the help for "@plugin help TeamMeteo" here
    This should describe *how* to use this plugin."""
    pass
    def __init__(self, irc):
        self.__parent = super(TeamMeteo, self)
        self.__parent.__init__(irc)

    def bmeteo(self,irc,msg,args):
        """takes no arguments

        Displays some data
        """
        irc.reply(str('coucou'))

Class = TeamMeteo


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:

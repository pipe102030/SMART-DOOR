# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

# Mycroft libraries
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import requests


__author__ = 'pipe102030'

LOGGER = getLogger(__name__)

class IotDoorSkill(MycroftSkill):


    def __init__(self):
        super(IotDoorSkill, self).__init__(name="IotDoorSkill")
		
    def initialize(self):
	self.load_data_files(dirname(__file__))

        Door_command_intent = IntentBuilder("DoorCommandIntent").require("DoorKeyword").require("Action").build()
        self.register_intent(Door_command_intent, self.handle_Door_command_intent)

    def handle_Door_command_intent(self, message):
        action_word = message.data.get("Action")
        LOGGER.info("Command word: " + action_word )
        if action_word == "open" :
		    self.speak_dialog("open.door")
		    r = requests.get('http://ip_here/door?cmd=1')
            
	elif action_word == "close":
		self.speak_dialog("close.door")
		r = requests.get('http://ip_here/door?cmd=0')
	else:
		self.speak("not sure about that")  	

    def stop(self):
        pass

def create_skill():
    return IotDoorSkill()

#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# It is provided as a simple shell to guide the student and
# assist with implementation for the Programming the Internet
# of Things exercises related to the functionality that it
# will eventually contain.
#

import logging

from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.data.ActuatorData import ActuatorData

class ActuatorAdapterManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self, useEmulator: bool = False):
		pass

	def sendActuatorCommand(self, data: ActuatorData) -> bool:
		pass
	
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		pass

	def _emulateActuation(self, data: ActuatorData):
		pass
		
	def _engageActuator(self, data: ActuatorData):
		pass
	
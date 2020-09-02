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
import random

from programmingtheiot.data.ActuatorData import ActuatorData

class BaseActuatorSimTask():
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, actuatorType: int = ActuatorData.DEFAULT_ACTUATOR_TYPE, simpleName: str = "Actuator"):
		pass
		
	def activateActuator(self, val: float) -> bool:
		pass
		
	def deactivateActuator(self) -> bool:
		pass
		
	def getLatestActuatorResponse(self) -> ActuatorData:
		pass
	
	def getSimpleName(self) -> str:
		pass
	
	def updateActuator(self, data: ActuatorData) -> bool:
		pass
		
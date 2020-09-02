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

from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator

from programmingtheiot.data.SensorData import SensorData

class PressureSensorSimTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self):
		pass
	
	def generateTelemetry(self) -> SensorData:
		pass
	
	def getTelemetryValue(self) -> float:
		pass
	
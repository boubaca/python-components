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

from programmingtheiot.data.SensorData import SensorData

class BaseSystemUtilTask():
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self):
		###
		# TODO: fill in the details here
		self.latestSensorData = None
		
		pass
	
	def generateTelemetry(self) -> SensorData:
		###
		# TODO: fill in the details here
		#
		# NOTE: Use self._getSystemUtil() to retrieve the value from the sub-class
		pass
		
	def getTelemetryValue(self) -> float:
		pass
	
	def _getSystemUtil(self) -> float:
		"""
		Template method implemented by sub-class.
		
		Retrieve the system utilization value as a float.
		
		@return float
		"""
		pass
		
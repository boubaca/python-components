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

from programmingtheiot.data.BaseIotData import BaseIotData

class SensorData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
	DEFAULT_VAL = 0.0
	DEFAULT_SENSOR_TYPE = 0
	
	# These are just sensor type samples - these can be changed however
	# you'd like; you can also create an enum representing the values
	HUMIDITY_SENSOR_TYPE = 1
	PRESSURE_SENSOR_TYPE = 2
	TEMP_SENSOR_TYPE = 3
		
	def __init__(self, sensorType = DEFAULT_SENSOR_TYPE, d = None):
		super(SensorData, self).__init__(d = d)
		pass
	
	def getSensorType(self) -> int:
		"""
		Returns the sensor type to the caller.
		
		@return int
		"""
		return self.sensorType
	
	def getValue(self) -> float:
		pass
	
	def setValue(self, newVal: float):
		pass
		
	def _handleUpdateData(self, data):
		pass

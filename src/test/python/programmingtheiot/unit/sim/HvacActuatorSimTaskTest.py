#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging
import unittest

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.HvacActuatorSimTask import HvacActuatorSimTask

class HvacActuatorSimTaskTest(unittest.TestCase):
	"""
	This test case class contains very basic unit tests for
	HvacActuatorSimTask. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	DEFAULT_VAL_A = 18.2
	DEFAULT_VAL_B = 21.4
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing HvacActuatorSimTask class...")
		self.hSimTask = HvacActuatorSimTask()
		
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testUpdateActuator(self):
		ad = ActuatorData(actuatorType = ActuatorData.HVAC_ACTUATOR_TYPE)
		ad.setCommand(ActuatorData.COMMAND_ON)
		ad.setValue(self.DEFAULT_VAL_A)
		adr = self.hSimTask.updateActuator(ad)
		
		if adr:
			self.assertTrue(adr.getValue(), self.DEFAULT_VAL_A)
			logging.info("ActuatorData: " + str(adr))
		else:
			logging.warning("ActuatorData is None.")
			
		ad.setValue(self.DEFAULT_VAL_B)
		adr = self.hSimTask.updateActuator(ad)
		
		if adr:
			self.assertTrue(adr.getValue(), self.DEFAULT_VAL_B)
			logging.info("ActuatorData: " + str(adr))
		else:
			logging.warning("ActuatorData is None.")
			
		ad.setCommand(ActuatorData.COMMAND_OFF)
		adr = self.hSimTask.updateActuator(ad)
		
		if adr:
			self.assertEquals(adr.getCommand(), ActuatorData.COMMAND_OFF)
			logging.info("ActuatorData: " + str(adr))
		else:
			logging.warning("ActuatorData is None.")
			
if __name__ == "__main__":
	unittest.main()
	
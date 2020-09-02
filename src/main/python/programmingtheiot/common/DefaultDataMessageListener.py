#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.common.IDataMessageListener import IDataMessageListener

class DefaultDataMessageListener(IDataMessageListener):
	"""
	Interface definition for data message listener clients.
	
	"""

	def handleMessage(self, topicEnum: ResourceNameEnum, msg: str) -> bool:
		"""
		Attempts to subscribe to a topic with the given qos hosted by the
		pub/sub broker / server. If not already connected, the sub-class
		implementation should either throw an exception, or handle the exception
		and log a message, and return False.
		
		@param topicEnum The topic Enum to subscribe to.
		@param msg The message received. It is expected to be in JSON format.
		@return bool True on success, False otherwise.
		"""
		print('Topic: %s, Message: %s', topicEnum.name, msg)

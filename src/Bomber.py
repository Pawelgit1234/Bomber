from abc import ABC, abstractmethod


class Bomber(ABC):
	@abstractmethod
	def __init__(self, receiver, min_interval, max_interval):
		self.receiver = receiver
		self.min_interval, = min_interval,
		self.max_interval = max_interval
		self.server = None

	@abstractmethod
	def start_bombing(self):
		return NotImplementedError("Its abstract method")

	@abstractmethod
	def start_DDOS_bombing(self):
		return NotImplementedError("Its abstract method")
class ROM(object):
	""" The ROM object representing the
		bytes contained in the loaded game.
	"""
	def __init__(self, filepath):
		self.bytes = []
		with open(filepath, "rb") as rom:
			byte = rom.read(1)
			while byte:
				self.bytes.append(byte.encode("hex").upper())
				byte = rom.read(1)

	def __getitem__(self, index):
		return self.bytes[index]

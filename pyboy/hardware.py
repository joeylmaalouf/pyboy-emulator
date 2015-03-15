class CPU(object):
	""" The object representation of the Game Boy's
		internal CPU, a custom Zilog Z80.
	"""
	def __init__(self, rom):
		self.memory = rom

		self.clocks = {"m":0, "t":0}

		self.registers = {
			"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "h":0, "l":0,  # 8-bit registers
			"pc":0, "sp":0,                                          # 16-bit registers
			"m":0, "t":0,                                            # Clocks for last instruction
			"ime":0
		}

		self.halt = 0
		self.stop = 0

	def reset(self):
		self.clocks["m"] = 0
		self.clocks["t"] = 0
		self.registers["a"] = 0
		self.registers["b"] = 0
		self.registers["c"] = 0
		self.registers["d"] = 0
		self.registers["e"] = 0
		self.registers["f"] = 0
		self.registers["h"] = 0
		self.registers["l"] = 0
		self.registers["pc"] = 0
		self.registers["sp"] = 0
		self.registers["m"] = 0
		self.registers["t"] = 0
		self.registers["ime"] = 1
		self.halt = 0
		self.stop = 0


class MMU(object):
	""" The object representation of the Game Boy's
		memory management unit. Bytes are 8 bits,
		words are 2 bytes (16 bits).
	"""
	def __init__(self):
		pass

	def read_byte(self, address):
		pass

	def read_word(self, address):
		pass

	def write_byte(self, address, value):
		pass

	def write_word(self, address, value):
		pass

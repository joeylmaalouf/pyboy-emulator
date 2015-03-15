class CPU(object):
	""" The object representation of the Game Boy's
		internal CPU, a custom Zilog Z80.
	"""
	def __init__(self, rom):
		self.game_rom = rom

		self.clocks = {"m":0, "t":0}

		self.registers = {
			"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "h":0, "l":0,  # 8-bit registers
			"pc":0, "sp":0,                                          # 16-bit registers
			"i":0, "r":0,
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
		self.registers["i"] = 0
		self.registers["r"] = 0
		self.registers["m"] = 0
		self.registers["t"] = 0
		self.registers["ime"] = 1
		self.halt = 0
		self.stop = 0

	def NOP(self):
		self.registers["m"] = 1                       # 1 M-time taken
		self.registers["t"] = 4

	def LD(self, par1, par2):
		self.registers[par1] = self.registers[par2]   # load value
		self.NOP()                                    # 1 M-time taken

	def ADD(self, par1, par2):
		self.registers[par1] += self.registers[par2]  # perform addition
		self.registers["f"] = 0                       # clear flags

		if not (self.registers[par1] & 255):          # check for zero
			self.registers["f"] |= 0x80

		if self.registers[par1] > 255:                # check for carry
			self.registers["f"] |= 0x10

		self.registers[par1] &= 255                   # mask to 8 bits
		self.NOP()                                    # 1 M-time taken

	def CMP(self, par1, par2):
		tmp = self.registers[par1]                    # create a temporary copy
		tmp -= self.registers[par2]                   # perform subtraction
		self.registers["f"] |= 0x40                   # set subtraction flag

		if not (tmp & 255):                           # check for zero
			self.registers["f"] |= 0x80
		if tmp < 0:                                   # check for underflow
			self.registers["f"] |= 0x10

		self.NOP()                                    # 1 M-time taken


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

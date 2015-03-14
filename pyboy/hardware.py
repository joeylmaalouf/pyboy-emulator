class CPU(object):
	""" The representation of the GameBoy's
		internal CPU, a custom Zilog Z80.
	"""
	def __init__(self):
		self.clocks = {"m":0, "t":0}
		self.registers = {
			"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "h":0, "l":0,  # 8-bit registers
			"pc":0, "sp":0,                                          # 16-bit registers
			"m":0, "t":0                                             # Clocks for last instruction
		}

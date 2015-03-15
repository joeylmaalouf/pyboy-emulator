""" Credits to:
	http://imrannazar.com/GameBoy-Emulation-in-JavaScript - for a great overview of how gameboys work internally
	http://gbdev.gg8.se/wiki/articles/The_Cartridge_Header - for the ROM header structure
	myself - for actually making this!
"""


from pyboy.loader import ROM
from pyboy.hardware import CPU
from sys import argv


def main(argv):
	if len(argv) < 2:
		print("Error: please provide a path to the ROM.")
	else:
		game = CPU(ROM(argv[1]))
		print("ROM \""+argv[1]+"\" loaded successfully!")
		print("Internal game name:  "+game.memory.name)
		print("Cartridge type:      "+game.memory.cartridge_type)
		print("ROM size:            "+game.memory.rom_size)
		print("RAM size:            "+game.memory.ram_size)
		print("Made only for Japan: "+game.memory.japanese)


if __name__ == "__main__":
	main(argv)

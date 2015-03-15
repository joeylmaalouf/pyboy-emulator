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
		game_rom = ROM(argv[1])
		game_cpu = CPU(game_rom)
		print("\nROM \""+argv[1]+"\" loaded successfully!\n")
		print("Internal game name:  "+game_rom.name)
		print("Cartridge type:      "+game_rom.cartridge_type)
		print("ROM size:            "+game_rom.rom_size)
		print("RAM size:            "+game_rom.ram_size)
		print("Made only for Japan: "+game_rom.japanese)
		print("")


if __name__ == "__main__":
	main(argv)

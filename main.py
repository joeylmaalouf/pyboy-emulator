from pyboy.loader import ROM
from pyboy.hardware import CPU
from sys import argv


def main(argv):
	if len(argv) < 2:
		print("Error: please provide a path to the ROM.")
	else:
		game = ROM(argv[1])


if __name__ == "__main__":
	main(argv)

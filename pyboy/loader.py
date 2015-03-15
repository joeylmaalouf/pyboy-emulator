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

		self.name = "".join(chr(int(b, 16)) for b in self.bytes[int("0x134", 16):int("0x143", 16)])

		self.cartridge_type = {
			0x00:"ROM ONLY",
			0x01:"MBC1",
			0x02:"MBC1+RAM",
			0x03:"MBC1+RAM+BATTERY",
			0x05:"MBC2",
			0x06:"MBC2+BATTERY",
			0x08:"ROM+RAM",
			0x09:"ROM+RAM+BATTERY",
			0x0B:"MMM01",
			0x0C:"MMM01+RAM",
			0x0D:"MMM01+RAM+BATTERY",
			0x0F:"MBC3+TIMER+BATTERY",
			0x10:"MBC3+TIMER+RAM+BATTERY",
			0x11:"MBC3",
			0x12:"MBC3+RAM",
			0x13:"MBC3+RAM+BATTERY",
			0x15:"MBC4",
			0x16:"MBC4+RAM",
			0x17:"MBC4+RAM+BATTERY",
			0x19:"MBC5",
			0x1A:"MBC5+RAM",
			0x1B:"MBC5+RAM+BATTERY",
			0x1C:"MBC5+RUMBLE",
			0x1D:"MBC5+RUMBLE+RAM",
			0x1E:"MBC5+RUMBLE+RAM+BATTERY",
			0xFC:"POCKET CAMERA",
			0xFD:"BANDAI TAMA5",
			0xFE:"HuC3",
			0xFF:"HuC1+RAM+BATTERY"
		}[self.int_val_at("0x147")]

		self.rom_size = {
			0x00:"32 KB (no ROM banking)",
			0x01:"64 KB (4 banks)",
			0x02:"128 KB (8 banks)",
			0x03:"256 KB (16 banks)",
			0x04:"512 KB (32 banks)",
			0x05:"1 MB (64 banks)",
			0x06:"2 MB (128 banks)",
			0x07:"4 MB (256 banks)",
			0x52:"1.1 MB (72 banks)",
			0x53:"1.2 MB (80 banks)",
			0x54:"1.5 MB (96 banks)"
		}[self.int_val_at("0x148")]

		self.ram_size = {
			0x00:"None",
			0x01:"2 KB",
			0x02:"8 KB",
			0x03:"32 KB"
		}[self.int_val_at("0x149")]

		self.japanese = str(not bool(self.int_val_at("0x14A")))


	def __getitem__(self, index):
		return self.bytes[index]


	def int_val_at(self, hex_address_str):
		return int(self[int(hex_address_str, 16)])

#Aarch64.reg file parsing utilities

import sys
import os
def setup_register_table():
	direct = os.getcwd()
	os.path.exists(direct)
	regFile = ""
	try:
		regFile = open(direct+"/Aarch64.reg", "r")
	except Exception as e:
		#sys.exit("ERROR: Failed to find Aarch64.reg file");
		print e
		return None

	try:
		lineNo = 0
		aarch64Registers = {
			"" : ""
		}
		for line in regFile:
			lineNo += 1
			if "//" in line or line == "":
				continue
			# encodings = line.split(",")
			# aarch64Registers[int(encodings[2],2)][int(encodings[3], 2)][int(encodings[4], 2)][int(encodings[5], 2)] = encodings[0]
			value = line.rstrip().split(',')
			name = value[0]
			bsEncoding = value[1] + value[2] + value[3] + value[4] + value[5]
			#iEncoding = int(bsEncoding, 2)
			if not str(bsEncoding) in aarch64Registers:
				aarch64Registers[str(bsEncoding)] = name
			else:
				print bsEncoding, "is already present, repeated value"
				return None
	except Exception as e:
			print e, "lineNo:", lineNo
			return None
	return aarch64Registers
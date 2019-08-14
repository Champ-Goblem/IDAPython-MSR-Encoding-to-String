import reg_parser
from idautils import *
from idaapi import *
from idc import *

def process_msr():
	aarch64Registers = reg_parser.setup_register_table()
	if aarch64Registers == None:
		return

	def decode_ins(sIns):
		hIns = ""
		for c in range(ItemSize(head), 0, -1):
			hIns += sIns[c-1].encode("hex")
		return str(bin(int(hIns, 16))[2:].zfill(8))

# 0                   9 10 11  12 13 15 16   19 20   23 24 26 27   31
#+---------------------+---+-----+-----+-------+-------+-----+------+
#| 1 1 0 1 0 1 0 1 0 0 | L | op0 | op1 |  CRn  |  CRm  | op2 |  Rt  |
#+---------------------+---+-----+-----+-------+-------+-----+------+
	for segeastart in Segments():
		print "Checking", SegName(segeastart)
		for funcea in Functions(segeastart, SegEnd(segeastart)):
		#for funcea in Functions(SegStart(ScreenEA()), SegEnd(ScreenEA())):
			for (startea, endea) in Chunks(funcea):
				for head in Heads(startea, endea):
					if GetMnem(head) == "MSR":
						#print "%X" % head
						sIns = GetManyBytes(head, ItemSize(head))
						ins = decode_ins(sIns)[11:27]
						try:
							comment =  aarch64Registers[ins]
						except Exception as e:
							if int(ins[0:2], 2) == 3 and (int(ins[5:9], 2) == 11 or int(ins[5:9], 2) == 15):
								comment = 'IMP_DEF'
						if comment != None:
							MakeComm(head, comment)
					elif GetMnem(head) == "MRS":
						#print "%X" % head
						sIns = GetManyBytes(head, ItemSize(head))
						ins = decode_ins(sIns)[11:27]
						try:
							comment = aarch64Registers[ins]
						except Exception as e:
							if int(ins[0:2], 2) == 3 and (int(ins[5:9], 2) == 11 or int(ins[5:9], 2) == 15):
								comment = 'IMP_DEF'
						if comment != None:
							MakeComm(head, comment)

	print "Done"
About
=====
This decodes MSR/MRS instructions in IDA and adds a comment with their corresponding register name to make it easier to read the disassembly rather than names in the form <code>op1, crn, crm, op2</code>

It uses register definitions taken from the LLVM mirror <a href="https://github.com/llvm-mirror/llvm/blob/efea7114d4f7bc56ab90df04037bdb7cd7d4f8c3/lib/Target/AArch64/AArch64SystemOperands.td">AArch64SystemOperands.td</a>

Running
=======
There is already an Aarch64.reg file provided in the repository but if it needs to be updated check Update heading

Firstly before running the script copy Aarch64.reg file to the current working directory where you will be disassembling your file with IDA

Then in IDA go to <code>File->Scirpt File</code> and select <code>ida_msr_string.py</code>

This should import the module into ida as <code>mes</code>

Finally run the script via <code>mes.process_msr()</code>

Reloading the module after changes
==================================
If you make any changes to the python file and have the module already loaded in IDA run <code>File->Script File</code> and select <code>ida_msr_string_reload.py</code>

Updating Aarch64.reg
====================
Download AArch64SystemOperands.td from above and remove all the lines from the top until you reach
<code>//===----------------------------------------------------------------------===//
// MRS/MSR (system register read/write) instruction options.
//===----------------------------------------------------------------------===//</code>

Then after that remove all lines that do not start with <code>def :</code>

Finally you need to remove these strings and characters:
<code>
	def :<br>
	ROSysReg<br>
	RWSysReg<br>
	WOSysReg<br>
	<<br>
	><br>
	"<br>
	;<br>
	0b<br>
</code>
You must also remove any space characters too

Easiest way to format this is to use the replace function of Sublime/Notepad++ or similar and put the characters in the Find box and nothing in the replace box so that the characters are removed.

The final register definitions should be of the format
<code>string name,bits<2> op0,bits<3> op1,bits<4> crn,bits<4> crm,bits<3> op2</code>
<b>NOTE! there should be no spaces between commas and values NOTE!</b>
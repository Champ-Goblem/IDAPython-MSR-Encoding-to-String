About
=====
This decodes MSR/MRS instructions in IDA and adds a comment with their corresponding register name to make it easier to read the disassembly rather than names in the form <code>op1, crn, crm, op2</code>

It uses register definitions taken from the LLVM mirror <a href="https://github.com/llvm-mirror/llvm/blob/efea7114d4f7bc56ab90df04037bdb7cd7d4f8c3/lib/Target/AArch64/AArch64SystemOperands.td">AArch64SystemOperands.td</a>

Usage
=====
There is already an Aarch64.reg file provided in the repository but if it needs to be updated check Update heading

Firstly before running the script copy Aarch64.reg file to the current working directory where you will be disassembling your file with IDA

Then in IDA go to <code>File->Script File</code> and select <code>ida_msr_string.py</code>

This should import the module into ida as <code>mes</code>

<b>Warning this will overwrite any comments you have already at any MSR/MRS instrcutions so be advised, any other instructions will not be touched though</b>

Finally run the script via <code>mes.process_msr()</code>

Depending on file size this could take a few minutes so theres time to grab a hot drink

Reloading the module after changes
==================================
If you make any changes to the python file and have the module already loaded in IDA run <code>File->Script File</code> and select <code>ida_msr_string_reload.py</code>

Updating Aarch64.reg
====================
Download AArch64SystemOperands.td from above and remove all the lines from the top until you reach
<pre>
<code>//===----------------------------------------------------------------------===//
// MRS/MSR (system register read/write) instruction options.
//===----------------------------------------------------------------------===//</code>
</pre>

Then after that remove all lines that do not start with <code>def :</code>

Finally you need to remove these strings and characters:
<pre>
<code>def :
ROSysReg
RWSysReg
WOSysReg
<
>
"
;
0b</code>
</pre>
You must also remove any space characters too

Easiest way to format this is to use the replace function of Sublime/Notepad++ or similar and put the characters in the Find box and nothing in the replace box so that the characters are removed.

The final register definitions should be of the format
<br><code>string name,bits<2> op0,bits<3> op1,bits<4> crn,bits<4> crm,bits<3> op2</code><br>
<b>NOTE! there should be no spaces between commas and values</b>

Comments are allowed in the Aarch64.reg file with format <code>//</code>

Adding IMPLEMENTATION DEFINED registers
======================================
Currently IMPLEMENTATION DEFINED registers will be shown as <code>IMP_DEF</code> in the comments section

In order to add a custom definition for these you can manual add a register defintion to Aarch64.reg file in the form
<br><code>string name,bits<2> op0,bits<3> op1,bits<4> crn,bits<4> crm,bits<3> op2</code><br>

Then to evalutate the file again you can run <code>mes.process_msr()</code> without needing to reload the python module

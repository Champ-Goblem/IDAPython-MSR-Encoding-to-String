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
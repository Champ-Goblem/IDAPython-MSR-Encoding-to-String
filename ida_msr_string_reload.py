import sys
for mod in sys.modules.keys():
    if 'ida_msr_string' in mod:
        del sys.modules[mod]

import ida_msr_string
import ida_msr_string as mes

print 'reloaded module as mes'
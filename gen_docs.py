#!/usr/bin/env python

import sys
import re
import os

pat_function = re.compile(r'\n[ ]*(\w+\([^)]*\))\s*{')
pat_class = re.compile(r'class (\w+)')

format_title = "{1}"
format_comment = ""
format_call = "  - {}.{}"
format_call_no_class = "  - {}{}"

def make_docs(path):
    local_format_call = format_call

    try:
        with file(path) as f:
            text = f.read()
    except IOError:
        return None
    
    try:
        file_class = pat_class.search(text).group(1)
    except AttributeError:
        file_class = ""
        local_format_call = format_call_no_class

    print format_title.format(*os.path.split(path))
    for m in pat_function.finditer(text):
        print local_format_call.format(file_class,  m.group(1))

    print

if __name__ == '__main__':
    for path in sys.argv[1:]:
        make_docs(path)



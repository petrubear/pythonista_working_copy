import difflib
#from difflib_data import *

text1 = """Lorem ipsum.
123"""

text1_lines = text1.splitlines()

text2 = """lorem Ipsum
127
blabla"""

text2_lines = text2.splitlines()


def do_diff():
  diff = difflib.Differ()
  result = diff.compare(text1_lines, text2_lines)
  print('\n'.join(result))


do_diff()


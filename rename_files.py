#! python3.70
'''
Append current YYYY-MMDD date format in sequence and rename all files in the current directory.

1. Current datetime will be used;
2. Iterates through a sequence beginning from 0001;
3. Maintains and appends to the original filename; and
4. Existing files starting with YYYY-MMDD will be skipped.
'''

import os
import datetime

path = os.getcwd()

filelist = os.listdir(path)

YMD = datetime.date.today().strftime("%Y-%m%d")

num = 1
for filename in filelist:
	ori_fname, fext = os.path.splitext(filename)	
	numseq = ("{:04d}".format(num))							# 4-digit numbering (0001:)
	new_fname = (f"{YMD} {numseq} {ori_fname} {fext}")		# ALT: (YMD + " " + ori_fname + fext)
	if filename.startswith(YMD):
		continue
	else:
		os.rename(filename, new_fname)
		num += 1


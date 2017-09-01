#!/usr/bin/python
  
import acq400_hapi
import os
import argparse
import sys


parser = argparse.ArgumentParser(description='run-fg: runs the function gen')
parser.add_argument('--awg', help="awg raw data file")
parser.add_argument('uut', nargs='+', help="uut")

args = parser.parse_args()
uut = acq400_hapi.Acq400(args.uut[0])

uut.load_awg(args.awg, autorearm=True)
uut.s1.trg = '1,1,1'
uut.s1.clk = '1,0,0'
uut.s1.clkdiv = 2       # 2MHz/2 = 1MSPS
uut.s0.SIG_SRC_TRG_1 = 'GPG1'
uut.s0.SIG_SRC_CLK_0 = 'HDMI'
uut.s0.SIG_SRC_TRG_0 = 'HDMI'



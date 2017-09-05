#!/usr/bin/python
  
import acq400_hapi
import os
import argparse
import sys


parser = argparse.ArgumentParser(description='run-fg: runs the function gen')
parser.add_argument('--awg', default="none", help="awg raw data file")
parser.add_argument('uut', nargs='+', help="uut")

args = parser.parse_args()
uut = acq400_hapi.Acq400(args.uut[0])

#if args.awg != "none":
#	uut.load_awg(args.awg, autorearm=True)

uut.s1.trg = '1,1,1'                # AWG TRG d1
uut.s1.clk = '1,0,0'                # AWG CLK d0
uut.s1.CLKDIV = '2'                 # 2MHz/2 = 1MSPS
uut.s0.SIG_EVENT_SRC_1 = 'GPG'      # front panel output for monitor.
uut.s0.SIG_SRC_TRG_1 = 'GPG1'       # AWG trigger is GPG1 (internal)
uut.s0.SIG_SRC_CLK_0 = 'HDMI'       # CLK is SLAVED
uut.s0.SIG_SRC_TRG_0 = 'HDMI'       # TRG is SLAVED



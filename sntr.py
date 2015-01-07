#!/usr/bin/python2.7

import sys, os, math, time

longitude = 122.3

LSTM = 15 * 8
def EOT():
	B = float(360.0/365.24) * (float(time.strftime('%j')) - 81)
	
	return (9.87 * math.sin(2 * float(B))) - (7.53 * math.cos(float(B))) - (1.5 * math.sin(float(B)))

def TCF(long):
	return (4 * (long - float(LSTM))) + EOT()

print ('EOT:%.6f' % EOT())
print ('TCF:%.6f' % TCF(longitude))

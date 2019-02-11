#!/usr/bin/python
import numpy as np

# Take input from user
print "Input x,y,z co-ordinates (space separated) for A B C & D (each on new line):"
P = [[float(i) for i in raw_input().split()] for j in range(4)]
P = np.array(P)

# ----------------------------------------------------------------- #
print "\nLength CD :",np.linalg.norm(P[2]-P[3]) # To print magnitude/length of CD
# ----------------------------------------------------------------- #

CB = P[1]-P[2]; CD = P[3]-P[2]
aBCD = np.dot(CB,CD) / (np.linalg.norm(CB) * np.linalg.norm(CD))
print "\xe2\x88\xa1 BCD :",np.degrees(np.arccos(aBCD))  # To print angle BCD

# ----------------------------------------------------------------- #
# Components of vector BA,BC & BD
BA=P[0]-P[1]; BC=P[2]-P[1]; BD=P[3]-P[1]
# Components of Vector Q1, Q2 & Q3
Q1 = np.cross(BC,BA)
Q2 = np.cross(BC,BD)
Q3 = np.cross(Q1,Q2)
# Torsion angle calculation
torsion= np.dot(Q1,Q2) / (np.linalg.norm(Q1)*np.linalg.norm(Q2))
torsion=np.degrees(np.arccos(torsion))	# Conversion to degrees
# Sign assignment to angle
if np.dot(Q3,BC)<0:
	print "Torsion angleABCD:",-torsion
else :
	print "Torsion angleABCD:",torsion
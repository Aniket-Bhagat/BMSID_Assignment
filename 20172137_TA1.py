#!/usr/bin/env python
import numpy as np

print "Input x,y,z co-ordinates (space separated) for A B & C (each on new line):"
P = [[float(i) for i in raw_input().split()] for j in range(3)]
P = np.matrix(P)

l = input("\ninput length of CD (armstrong) : ")
T = 180-input("\ninput angle BCD (degrees): ")
X = input("\ninput torsion angle ABCD (degrees): ")

b = P[1:] - P[:-1]
# Components of vector AB & BC is p & q respectively :
p=b[0]; q=b[1]
# print "Components of vector AB :",p
# print "Components of vector BC :",q

# To get unit vector 'n' along plane A-B-C:
PxQ = np.cross(p,q)		# CrossProduct of vector p & q
n = PxQ / np.linalg.norm(PxQ)
# print "Unit Vector Normal to plane A-B-C :",n

# To get unit vector 'u' along direction 'q':
u = q / np.linalg.norm(q)
# print "Unit Vector along direction of BC vector :",u

# To get component vector CD along direction q :
v = l * u

# Function for Matrix expression for effect of rotation 
# of co-ordinates of point in space with angle theta 
def JJmatrix(t,x,y,z):
	a = np.cos(np.radians(t)) + (x**2)*(1-np.cos(np.radians(t)))
	b = x*y*(1-np.cos(np.radians(t))) - z*np.sin(np.radians(t))
	c = x*z*(1-np.cos(np.radians(t))) + y*np.sin(np.radians(t))
	d = x*y*(1-np.cos(np.radians(t))) + z*np.sin(np.radians(t))
	e = np.cos(np.radians(t)) + (y**2)*(1-np.cos(np.radians(t)))
	f = y*z*(1-np.cos(np.radians(t))) - x*np.sin(np.radians(t))
	g = x*z*(1-np.cos(np.radians(t))) - y*np.sin(np.radians(t))
	h = y*z*(1-np.cos(np.radians(t))) + x*np.sin(np.radians(t))
	i = np.cos(np.radians(t)) + (z**2)*(1-np.cos(np.radians(t)))
	return np.matrix([[a,b,c],[d,e,f],[g,h,i]])

# Function to calculate Direction Cosines
def DiCo(V):
	d = V / np.linalg.norm(V)
	lamda = d[0,0]; mu = d[0,1]; neu = d[0,2]
	return [lamda,mu,neu]

# Direction cosines calculations
U = DiCo(u)
N = DiCo(n)

M1 = JJmatrix(X,U[0],U[1],U[2])
M2 = JJmatrix(T,N[0],N[1],N[2])

print "\n--------------------------------------------------------------------------------"
print "Co-ordinates of D :",(P[2].T+M1*M2*v.T).T
print "--------------------------------------------------------------------------------"

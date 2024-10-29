# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
#   finds the intersection point (if it exists) between a ray and the Earth reference ellipsoid

# Parameters:
#   d_l_x: x-coordinate of origin referenced ray unit vector
#   d_l_y: y-coordinate of origin referenced ray unit vector
#   d_l_z: z-coordinate of origin referenced ray unit vector
#   c_l_x: x-coordinate of ray origin offset
#   c_l_y: y-coordinate of ray origin offset
#   c_l_z: z-coordinate of ray origin offset

# Output:
#   x-component, y-component, and z-component of intersection point
#
# Written by Grant Chapman
# Other contributors: None

# import Python modules
import sys
import math

# constants
R_E_KM = 6378.137
E_E    = 0.081819221456

# initialize script arguments
d_l_x = float('nan')
d_l_y = float('nan')
d_l_z = float('nan')
c_l_x = float('nan')
c_l_y = float('nan')
c_l_z = float('nan')

# parse script arguments
if len(sys.argv) == 7:
  d_l_x = int(sys.argv[1])
  d_l_y = int(sys.argv[2])
  d_l_z = int(sys.argv[3])
  c_l_x = int(sys.argv[4])
  c_l_y = int(sys.argv[5])
  c_l_z = int(sys.argv[6])
else:
  print(\
    'Usage: '\
    'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
  )
  exit()

## script below this line

## discriminant
a = d_l_x**2 + d_l_y**2 + d_l_z**2/(1-E_E**2)
b = 2.0*(d_l_x*c_l_x + d_l_y*c_l_y + d_l_z*c_l_z/(1-E_E**2))
c = c_l_x**2 + c_l_y**2 + c_l_z**2/(1-E_E**2) - R_E_KM**2
discr = b**2 - 4.0*a*c

## solution logic
if discr >= 0.0:
  d = (-b - math.sqrt(discr))/(2.0*a)
  if d < 0.0:
    d = (-b + math.sqrt(discr))/(2.0*a)
  if d >= 0.0:
    l_d = [d*d_l_x+c_l_x, d*d_l_y+c_l_y, d*d_l_z+c_l_z]
    print(l_d[0])
    print(l_d[1])
    print(l_d[2])
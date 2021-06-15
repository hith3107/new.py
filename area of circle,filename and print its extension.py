
r=float(input("input the radius of circle:",))
import math
A=math.pi*r**2;
print("The area of circle with radius", end = '')
print(float(r),end = ' ')
print("is:",A)

filename=input("input the filename:",)
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))



# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:51:53 2024

@author: EO005063
"""

import numpy as np
import matplotlib.pyplot as plt
import os

file_location=os.path.join('deform_data.txt')
data=np.genfromtxt(fname=file_location,dtype="unicode",delimiter=",")
strain=data[2:,0]
z_strain=[]
for j in range(0,len(strain)):
    element=float(strain[j][1:])
    element=element*100
    z_strain.append(element)
stress=data[2:,3]
z_stress=[]
for i in range(0,len(stress)):
    element=stress[i][0:len(stress[i])-3]
    element=float(element)
    z_stress.append(element)
plt.figure()
plt.xlabel("Strain(%)")
plt.ylabel("Stress in Z direction(GPa)")
plt.ylim(0,75)
plt.xlim(0,35)
plt.plot(z_strain,z_stress)
plt.savefig("Strain_Stress.png",dpi=300)


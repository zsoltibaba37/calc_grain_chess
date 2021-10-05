#!/usr/bin/env python
# coding: utf-8

# ## Rice weight calc - ``Fibonacci``
# 
# Calculated the weight of last field of rice, by adding the previous two field in each step.

# In[21]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

count = 64

# one rice grain weights
rice = 0.021

def find_fib(n, computed = {0: 1, 1: 2}):
    if n not in computed:
        computed[n] = find_fib(n-1, computed) + find_fib(n-2, computed)
    return computed[n]

# start = time()
nums = []
for i in range(count):
    a = find_fib(i)
    nums.append(a)
# end = time()
n = str(nums[-1:]).strip('[*]')
num = float(n)

print("Put one rice grain to first field. Put two rice the second place. Add first and second field.")
print("How much rice will be in the last field?\n")

print(f"Last field rice weight: {(num*rice)/10**3 :.0f} kg")
print(f"Last field rice weight: {(num*rice)/10**6 :.0f} tons")


# <!-- ![chess](./chess.jpg) -->
# <img src="./chess.jpg" alt="chess" width="400"/>

# In[17]:


import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import math
figure(figsize=(8, 8), dpi=100)
from numba import njit

@njit(fastmath=True)
def rotate(point, ang):
    px = point
    angle = ang
    mathcos = math.cos(angle) * (px)
    mathsin = math.sin(angle) * (px)
    qx = mathcos - mathsin
    qy = mathsin + mathcos
    return qx, qy

angle = 0
coordx = []
coordy = []
for i in nums:
    qx, qy = rotate(i, angle)
    coordx.append(qx)
    coordy.append(qy)
    angle = angle + 45
    plt.plot(coordx, coordy, linestyle='--', marker='o', color='g', markersize=6,)

plt.show()


# ## Wheat and chessboard problem
# 
# Calculate the wheat of weight, if double the wheat in every place.

# In[67]:


count = 64

# one wheat grain weights
wheat = 0.065

num = 1
for i in range(1, count):
    num += 2**i
    
print("\nPut one wheat grain to first field. Double it in every step.")
print("What is the weight of the wheat on the chessboard?\n")

print(f"Weight of wheat: {(num*wheat)/10**3 :.0f} kg")
print(f"Weight of wheat: {(num*wheat)/10**6 :.0f} tons")

wheatWeight = (num*wheat)/10**6
# Production in 2014
in2014 = 729000000
# Production in 2019
in2019 = 780800000
print(f"\n{wheatWeight/in2014 :.0f} times more than production in 2014")
print(f"{wheatWeight/in2019 :.0f} times more than production in 2019")


#!/usr/bin/env python
# coding: utf-8

# In[21]:


import sympy as sp
#sp.init_printing()
import numpy as np

x, y, z = sp.symbols("x:z")

ex = x**2 + 2*y + z
print(ex)
k = ex.subs([(x, 1), (y, 2), (z, 3)])
print(k)
p = ex.subs({x:1, y: 2, z:3})
print(p)


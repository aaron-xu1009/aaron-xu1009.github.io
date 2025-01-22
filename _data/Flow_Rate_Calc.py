#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
syringe_dia_mm = float(input('Please input syringe diameter in mm '))
flow_rate = float(input('Please input the desired flow rate in mL/min '))
syringe_dia_cm = syringe_dia_mm / 10
flow_rate_s = flow_rate / 60
area = 0.25 * ((syringe_dia_cm) ** 2) * math.pi
vol = area * 0.004
sps = flow_rate_s/vol
print(f'Set steps per second to {sps:.2f}')


# In[ ]:





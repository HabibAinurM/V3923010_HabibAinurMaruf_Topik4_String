#!/usr/bin/env python
# coding: utf-8

# In[30]:


name = 'habibainurmaruf'

pjg = len (name)
print("panjang nama lengkap= ", pjg)

vokal = "aiueoAIUEO"
pjgvokal= len ([char for char in name if char in vokal])
print("panjang huruf vokal= ", pjgvokal)

konsonan= pjg - pjgvokal
print("panjang konsonan= ",konsonan)


# In[32]:


nama = input ("masukkan nama anda= ")

pjg = len (nama.replace(" ", ""))

vokal = "aiueoAIUEO"
pjgvokal= len ([char for char in name if char in vokal])

konsonan= pjg - pjgvokal

print("panjang nama lengkap= ", pjg)
print("panjang huruf vokal= ", pjgvokal)
print("panjang konsonan= ",konsonan)


# In[ ]:





# In[ ]:





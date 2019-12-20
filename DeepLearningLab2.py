#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(1)


# In[ ]:





# In[7]:


import time
i=0
start_time=time.time()
for i in range(0,110000):
    print(i)
end_time=time.time()
diff=end_time-start_time
print(diff)
    


# In[9]:


def cube(i):
    return(i**3)

i=0
for i in range(1,11):
    x=cube(i)
    print(x)
    i=i+1


# In[2]:


import math as m


# In[4]:



print(m.sqrt(100))
print(m.log(100))
print(m.factorial(5))
print(m.pow(5,2))
print(m.log(100,2))
print(m.gcd(25,5))

#comment the error 
#explore how to define default value for a function
#prepare a file ,formats can be CSV ,txt,pdf,prepare download csv file


# In[1]:


#print(range(10))
for i in range(1,11):
    print(i*i*i) 


# In[2]:


i=0
while(i<11):
    i=i+1
    print(i**3)


# In[4]:


i=0
while(i<11):
    i=i+1
    print(i**3)


# In[3]:


#print(range(10))
for i in range(1,11):
    print(i*i*i) 


# In[ ]:





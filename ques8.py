
# coding: utf-8

# In[106]:

import numpy as np
import matplotlib.pyplot as plt


output = 'b'


def cal_cdf(s):
    s.sort()
    cdf = []
    key = []
    sample_size = len(s)
#     #print(s)
    s.append(-1)
#     #print(s)
    
    i = 0
    while(i < sample_size):
        
        while(s[i] == s[i+1]):
            i = i+1 
                        

        key.append(s[i]) 
        cdf.append(float((i+1)/sample_size) )
        i = i+1


#     #print(key,cdf)
    return key,cdf
    


# ### Comparison between Normal based CI and DKW CI

# In[122]:

import pandas as pd



# In[119]:

## function to calculate Normal based CI
import math 
def cal_normal_CI(cdf):
    Z_val = 1.96 # for alpha=0.05
    U= []
    L= []
    n = len(cdf)
    for item in cdf:
        se = math.sqrt((item*(1-item))/n)
        L.append(item - Z_val*se)
        U.append(item + Z_val*se)
    
    #print(U,L)
    return U,L
    


# In[120]:

#function to calculate DKW based CI
def cal_DKW_CI(cdf):
    alpha = 0.05
    U= []
    L= []
    n = len(cdf)
    epsilon = math.sqrt((math.log(2/alpha))/(2*n))
    for item in cdf:
        L.append(item - epsilon)
        U.append(item + epsilon)
    
    #print(U,L)
    return U,L


# In[123]:

if(output=='a'):
    
    data = pd.read_csv('q8.csv')
    #data.describe()
    
    key, cdf = cal_cdf(data['x'].tolist())
    upper_norm_CI, lower_norm_CI = cal_normal_CI(cdf)
    #upper_DKW_CI, lower_DKW_CI = cal_DKW_CI(cdf)

    #plt.figure(figsize=(20,20))
    plt.figure('Cumulative Distribution')
    plt.plot(key,cdf,color='black')

    plt.plot(key,upper_norm_CI,color='red')
    plt.plot(key,lower_norm_CI,color='red')

    #plt.plot(key,upper_DKW_CI,color='green')
    #plt.plot(key,lower_DKW_CI,color='green')

    plt.xlabel('x')
    plt.ylabel('Pr[X<=x]')
    plt.title('Normal based CI (Red). Black line is the original distribution')
    plt.xlim(0,2)
    plt.ylim(0,1)
    plt.grid()
    plt.show()
    


# In[117]:


if(output=='b'):
    
    
    data = pd.read_csv('q8.csv')
    #data.describe()
    
    key, cdf = cal_cdf(data['x'].tolist())
    upper_norm_CI, lower_norm_CI = cal_normal_CI(cdf)
    upper_DKW_CI, lower_DKW_CI = cal_DKW_CI(cdf)

    #plt.figure(figsize=(20,20))
    plt.figure('Cumulative Distribution')
    plt.plot(key,cdf,color='black')

    plt.plot(key,upper_norm_CI,color='red')
    plt.plot(key,lower_norm_CI,color='red')

    plt.plot(key,upper_DKW_CI,color='green')
    plt.plot(key,lower_DKW_CI,color='green')

    plt.xlabel('x')
    plt.ylabel('Pr[X<=x]')
    plt.title('Comparison of Normal based CI (Red) and DKW based CI (Green). Black line is the original distribution')
    plt.xlim(0,2)
    plt.ylim(0,1)
    plt.grid()
    plt.show()


# In[ ]:




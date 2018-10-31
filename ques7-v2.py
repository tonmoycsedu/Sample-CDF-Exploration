
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt


# In[107]:

output = 'c' ###possible values = a,b,c,d. put a for ques 7(a), b for 7(b) and so on.


# #### See the effect of sample size on empirical pdf

# In[3]:


def cal_cdf(s):
    s.sort()
    cdf = []
    key = []
    sample_size = len(s)
    #print(s)
    s.append(-1)
    #print(s)
    
    i = 0
    while(i < sample_size):
        
        while(s[i] == s[i+1]):
            i = i+1 
                        

        key.append(s[i]) 
        cdf.append(float((i+1)/sample_size) )
        i = i+1


    #print(key,cdf)
    return key,cdf
    


# In[94]:

def prepend_zero(key,cdf):
    low = key[0]
    #print(low)
    if(low > 0):
        arr = np.zeros(int(low))
        
        cdf = arr.tolist()+cdf
        
        arr = np.fromfunction(lambda i: i, (int(low),))
        
        key = arr.tolist()+key
        
        
    return key,cdf


# In[95]:

def append_zero(key,cdf):
    high = key[len(key)-1]
    #print(high)
    index = 199-high
    #print(index)
    if(high < 199):
        arr = np.ones(int(index))
        #print(arr)
        cdf = cdf+arr.tolist()
        
        arr = np.fromfunction(lambda i: high+i, (int(index),))
        #print(arr)
        key = key+arr.tolist()
        
        
    return key,cdf


# In[98]:

if(output == 'a'):
    s = [2,3,4,1,7,8,9,1,5,4,4,1,2]
    key, cdf = cal_cdf(s)
    key, cdf = prepend_zero(key,cdf)
    
    plt.figure('Effect of incresing sample size on F')
    plt.plot(key,cdf)
    plt.scatter(key,np.zeros(len(key)),marker='x')
    plt.xlim(0,key[len(key)-1])
    plt.ylim(0,1)
    plt.xlabel('X')
    plt.ylabel('Pr[X<=x]')
    plt.title('Empirical CDF')
    #plt.grid()
    plt.show()
    
    


# In[100]:

if(output == 'b'):
    
    s = np.random.binomial(199,0.5,10) ##( binomial number generator with n=199,p=0.5,size =10
    key1, cdf1 = cal_cdf(s.tolist())
    key1, cdf1 = prepend_zero(key1,cdf1)
    key1, cdf1 = append_zero(key1,cdf1)
    
    s = np.random.binomial(199,0.5,100)
    key2, cdf2 = cal_cdf(s.tolist())
    key2, cdf2 = prepend_zero(key2,cdf2)
    key2, cdf2 = append_zero(key2,cdf2)

    s = np.random.binomial(199,0.5,1000)
    key3, cdf3 = cal_cdf(s.tolist())
    key3, cdf3 = prepend_zero(key3,cdf3)
    key3, cdf3 = append_zero(key3,cdf3)

    s = np.random.binomial(199,0.5,10000)
    key4, cdf4 = cal_cdf(s.tolist())
    key4, cdf4 = prepend_zero(key4,cdf4)
    key4, cdf4 = append_zero(key4,cdf4)
    
    ##Plot subgraphs
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,figsize=(15,8))
    f.subplots_adjust(hspace=0.5)
    f.suptitle('Effect of incresing sample size on F')
    ax1.plot(key1, cdf1)
    ax1.set_title("n=10")
    ax2.plot(key2, cdf2)
    ax2.set_title("n=100")
    ax3.plot(key3, cdf3)
    ax3.set_title("n=1000")
    ax4.plot(key4, cdf4)
    ax4.set_title("n=10000")

    ax1.set(xlabel='x', ylabel='Pr[X<=x]',ylim=(0,1),xlim=(0,key1[len(key1)-1]))
    ax2.set(xlabel='x', ylabel='Pr[X<=x]',ylim=(0,1),xlim=(0,key2[len(key2)-1]))
    ax3.set(xlabel='x', ylabel='Pr[X<=x]',ylim=(0,1),xlim=(0,key3[len(key3)-1]))
    ax4.set(xlabel='x', ylabel='Pr[X<=x]',ylim=(0,1),xlim=(0,key4[len(key4)-1]))
    plt.show()
    



# ### Effect of number of student on empirical CDF

# In[113]:

#m=10000
import collections

def cal_avg_cdf(m,binomial):
    keys = []
    cdfs = []
    for i in range(m):
        if(binomial):
            s = np.random.binomial(199,0.5,10)
            
        else:
            s = np.random.rand(10)
            
        key, cdf = cal_cdf(s.tolist())  
        
        key, cdf = prepend_zero(key,cdf)
        #key, cdf = append_zero(key,cdf)
        
        keys += key
        cdfs += cdf

    #print(keys)

    #print(cdfs)
    #print("######")
    final_keys = []
    final_cdfs = []
    for item in keys:
        #print(item)
        if (item not in final_keys):
            indices = [i for i, x in enumerate(keys) if x == item]
            val = 0
            for index in indices:
                val = val+ cdfs[index]

            final_keys.append(item)
            final_cdfs.append(float(val/len(indices)))

    #print(final_keys)
    #print(final_cdfs)
    final = {}
    for i in range(len(final_keys)):
        #print(final_keys[i],final_cdfs[i])
        final[final_keys[i]] = final_cdfs[i]

    #print(final)
    
    sorted_final = collections.OrderedDict(sorted(final.items()))
    #print(sorted_final)
    return sorted_final

    


# In[114]:

if(output == 'c'):
    s1 = cal_avg_cdf(10,0) ###parameter m, 1 for binomial number
     
    key1= list(s1.keys())
    
    plt.title('Empirical CDF with n=10,m=10,random numbers')
    plt.plot(list(s1.keys()),list(s1.values()))
    #plt.scatter(key1,np.zeros(len(key1)),marker='x')
    plt.xlim(0,key1[len(key1)-1])
    plt.ylim(0,1)
    plt.xlabel('X')
    plt.ylabel('Pr[X<=x]')
    #plt.title('Empirical CDF')
    #plt.grid()
    plt.show()
    


# In[ ]:

if(output == 'd'):
    s1 = cal_avg_cdf(10,1) ###parameter m
    s2 = cal_avg_cdf(100,1)
    s3 = cal_avg_cdf(1000,1)
    s4 = cal_avg_cdf(10000,1)
    
    key1= list(s1.keys())
    key2= list(s2.keys())
    key3= list(s3.keys())
    key4= list(s4.keys())
    
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,figsize=(15,8))
    f.subplots_adjust(hspace=0.5)
    f.suptitle('Effect of incresing student number on F')
    ax1.plot(list(s1.keys()),list(s1.values()))
    ax1.set_title("n=10,m=10")
    ax2.plot(list(s2.keys()),list(s2.values()))
    ax2.set_title("n=10,m=100")
    ax3.plot(list(s3.keys()),list(s3.values()))
    ax3.set_title("n=10,m=1000")
    ax4.plot(list(s4.keys()),list(s4.values()))
    ax4.set_title("n=10,m=10000")
    
    ax1.set(xlabel='x', ylabel='Pr[X<=x]',ylim=(0,1),xlim=(0,key1[len(key1)-1]))
    ax2.set(xlabel='x', ylabel='Pr[X<=x]',ylim=(0,1),xlim=(0,key2[len(key2)-1]))
    ax3.set(xlabel='x', ylabel='Pr[X<=x]',ylim=(0,1),xlim=(0,key3[len(key3)-1]))
    ax4.set(xlabel='x', ylabel='Pr[X<=x]',ylim=(0,1),xlim=(0,key4[len(key4)-1]))

#     ax1.set(xlabel='x', ylabel='Pr[X<=x]')
#     ax2.set(xlabel='x', ylabel='Pr[X<=x]')
#     ax3.set(xlabel='x', ylabel='Pr[X<=x]')
#     ax4.set(xlabel='x', ylabel='Pr[X<=x]')

    plt.show()



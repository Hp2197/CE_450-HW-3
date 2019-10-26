
# coding: utf-8

# In[1]:


def cnt_cd(f):
    def result(n):
        count=0
        for i in range(1,n+1):
            if(f(n,i)):
                count+=1
        return count

    return result
def is_prime(n,i):
    if(i==1):
        return 0
    if(i==2):
        return 1
    print("i",i)
    for x in range(2,i):    
        if(i%x==0):
            return False
    return True



print(cnt_cd (lambda n, i: n % i == 0)(12))
print(cnt_cd (lambda n, i: n % i == 0)(2)) 
print(cnt_cd (is_prime)(20)) 


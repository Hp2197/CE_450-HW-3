
# coding: utf-8

# In[1]:


def card_sum(n):
    a=[]
    result=0
    while True:
        if(n<10):
            a.append(n)
            break
        a.append(n%10)
        n=n//10
    
    for i in range(len(a)-1,-1,-1):
        if(i%2==1):
        
            a[i]=a[i]*2
            if(a[i]>9):
                s1=a[i]%10
                s2=a[i]//10
                a[i]=s1+s2 
        result+=a[i]
    return result
print(card_sum (138743))
print(card_sum (5105105105105100))
print(card_sum (4012888888881881))


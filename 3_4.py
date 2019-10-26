
# coding: utf-8

# In[1]:


def smth(g, dx): 
    def f(x):
        
        return (g(x-dx)+g(x)+g(x-dx))/3 
    return f        

square = lambda x:x**2
print(round(smth(square,1)(0),3))


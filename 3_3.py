
# coding: utf-8

# In[1]:


def f(): 
    def f1():
        def f2(x):
            def f3():
                return x
            return f3
        return f2
    return f1

print(f()()(3)())


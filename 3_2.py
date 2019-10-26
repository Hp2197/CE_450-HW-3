
# coding: utf-8

# In[2]:


def add(g1, g2):
    def result(x):
        return g1(x)+g2(x)
    return result

identity=lambda x:x
squre=lambda x:x**2
a1= add(identity,squre)
print(a1(4))
a2 = add (a1, identity)
print(a2(4))


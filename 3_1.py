
# coding: utf-8

# In[1]:


def square(x):
    return x*x
def triple(x):
    return 3*x
def identity(x):
    return x
def increment(x):
    return x+1
def intscts(f, x):
    def compare(s):
        if(f(x)==s(x)):
            return True
        else:
            return False
    return compare
at_three = intscts (square, 3)
print(at_three(triple)) 
print(at_three(increment)) 
at_three = intscts (identity, 1)
print(at_three(square))


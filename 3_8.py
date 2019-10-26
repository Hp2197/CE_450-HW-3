
# coding: utf-8

# In[1]:


def add_one(x):
    return x + 1
def times_two(x):
    return x * 2
def add_three(x):
    return x + 3

def cyc(g1, g2, g3):
    def times(count):
        def excute(x):
            a=0
           
            for i in range(0,count):
                
                if(a==0):
                    x=add_one(x)
                if(a==1):
                    x=times_two(x)
                if(a==2):
                    x=add_three(x)
                if(a%3==0 and i!=0):
                    x=add_one(x)
                if(a>2):
                    a=a%3
                
               
                a=a+1
            return x
        return excute
    return times


my_cyc = cyc(add_one, times_two, add_three)
h= my_cyc(0)
print(h(5))
h = my_cyc(6)
print(h(1))
h = my_cyc(3)            
print(h(2)) 


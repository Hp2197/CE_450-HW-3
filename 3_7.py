
# coding: utf-8

# In[1]:


from operator  import *
global AO

AO=[]

for i in range(97,123):
    AO.append(chr(i))
for i in range(65,91):
    AO.append(chr(i))

def letter_to_n(x):
    for a in range(0,len(AO)+1):
        if (AO[a]==x):
            return a

        
def n_to_letter(x): 
    return AO[x]
def generator(n, operation):
    def result(letter):
    	return AO[operation(letter_to_n(letter),n)]	
    	
    
    return result

print(letter_to_n('a'))
print(letter_to_n('c'))
print(n_to_letter(3))
h=generator(2,add)
print(h('a'))
h = generator(3, sub)
print(h('d'))


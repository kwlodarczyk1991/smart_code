def Hello_World(): 

    return "Hello,World" 
print(Hello_World())

name = "Paula"
def Hello(name): 
    
    if name: 
        return "Hello,World" 
    else: 
        return ("Hello " +  name) 
print (Hello(name))  

def print_Hello(name): 
    return ('Hello ' + name) 
print(print_Hello(name)) 

#hello.py 

import sys  

print('Number of arguments:',len(sys.argv), 'arguments') 
print('Argumensts list',str(sys.argv))
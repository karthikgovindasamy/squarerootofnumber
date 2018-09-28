# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 08:31:51 2018

@author: karthik G
"""
epsilon=0.0001
def alka(S,x):
    while(abs(x**2-S)>epsilon):
        xnext=(x + float(S)/x)/2
        x=xnext;   
    return x

initial_guess=1

print '-'*3,'-'*12
for i in range(1,100):
    if(initial_guess**2 < i):
       initial_guess=initial_guess+1
    print '|'+str(i),'|'+str(alka(i,initial_guess))+'|'

print '-'*3,'-'*12
        
         

    

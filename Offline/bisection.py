# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 21:02:07 2021

@author: User
"""

import math
import numpy as np
def fun(x):
    x1=x/(1-x) * math.sqrt(6/(2+x))
    return x1-0.05

def bisection(low,up,app_error,max_itr):
    if(fun(low)*fun(up)>=0):
        print("Not proper selection")
        return
    else:
        c1=None
        itr=0
        while(True):
            itr=itr+1
            if(itr>max_itr):
                break
            
            
            c2=(low+up)/2
            #print(c2)
            if(c1!=None):
                if( np.abs((c2-c1)/c2) <app_error ):
                    break
            c1=c2
            if(fun(c2)==0.0):
                break
            
            if(fun(c2)*fun(a)<0):
                up=c2
            else:
                low=c2
    return c2
            
            
            
        
    
   
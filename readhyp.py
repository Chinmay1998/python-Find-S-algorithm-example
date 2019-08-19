#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:49:07 2019

@author: exam
"""

import csv 
with open("data.csv","r") as csfile:
    csvreader = csv.reader(csfile)
    mylist=list(csvreader)
    h=['o','o','o','o','o','o']
    for r in mylist:
        j=0
        if r[-1]=='yes':
            for x in r:
                if x!='yes':
                    if h[j]=='o' and h[j]!=x:
                        h[j]=x
                    elif h[j]!='o' and h[j]!=x:
                        h[j]='?'
                    else:
                        pass
                    j=j+1
    print (h)
                        
                    
                            
    
                    
                
                
        

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 01:01:44 2020

@author: m1827
九连环拆解和组合方法
"""

def num_ring(num):
    ring = 'n%d'
    rings = list(range(num))
    for i in range(num):
        rings[i] = ring % int(i+1)
    return rings

def jiulianhuan(rings, up = False):
    global count
    count+=1
    num = len(rings)
    if up :
        if num <= 2:
            print('上', rings)
        else:
            jiulianhuan(rings[:num-1], up = True)
            jiulianhuan(rings[:num-2], up = False)
            print('上', rings[num-1])
            jiulianhuan(rings[:num-2], up = True)
    else:
        if num<=2:
            print('下', rings)
        else:
            jiulianhuan(rings[:num-2], up = False)
            print('下', rings[num-1])
            jiulianhuan(rings[:num-2], up = True)
            jiulianhuan(rings[:num-1], up = False)



temp = int(input('How many rings do you play?\n:'))
ring_all=num_ring(9)   
count = 0
jiulianhuan(ring_all, up = False)
print('The total opration cycle is',str(count))
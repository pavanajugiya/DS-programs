#-*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:16:43 2026

@author: pavan
"""
#h1)
size=8
p_list=[]


def push(product):
    if len(p_list)==size:
        print("Belt is Full")
    else:
        p_list.append(product)
        print(f"{product} is add..")
        
def peek():
    if p_list:
        print(f"top product {p_list[0]}")
    else:
        print("Belt is empty")
        
def update(product):
    if p_list:
        p_list[0]=product
        print("top product updated")
        print(p_list)
    else:
        print("Belt is empty")
    
def is_full():
    if len(p_list)==size:
        print("Belt is Full")
    else:
        
        print("space is available")
push('pavan')
push("harpal")
push("mahi")
push("aafridi")
peek()
update('swati')
is_full()


#h2)
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:27:19 2026

@author: pavan
"""

size = 5
q = [None] * size
f = -1
r = -1

def enq(vehicle):
    global f, r

    if (r + 1) % size == f:
        print("tol full")
        return

    if f == -1:
        f = r = 0
    else:
        r = (r + 1) % size

    q[r] = vehicle
    print(vehicle, "entered.")

def deq():
    global f, r

    if f == -1:
        print("tol Empty")
        return

    print(q[f], "left.")

    if f == r:
        f = r = -1
    else:
        f = (f + 1) % size

def dis():
    if f == -1:
        print("tol Empty")
        return

    print("Vehicles:",end='')
    i = f
    while True:
        print(q[i], end=" ")
        if i == r:
            break
        i = (i + 1) % size
    print()



enq("mansi")
enq("rahul")
enq("khushi")
enq("harpal")
enq("takshil")
dis()
deq()
deq()
dis()


#h3)
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:28:58 2026

@author: pavan
"""

b = []
f = []
cur = "House"

def visit(place):
    global cur
    b.append(cur)
    cur = place
    f.clear()
    print("cur Location:", cur)

def back():
    global cur
    if not b:
        print("No Previous Location")
    else:
        f.append(cur)
        cur = b.pop()
        print("cur Location:", cur)

def forward():
    global cur
    if not f:
        print("No Forward Location")
    else:
        b.append(cur)
        cur = f.pop()
        print("cur Location:", cur)

visit("theater")
visit("school")
visit("collage")
back()
back()
forward()



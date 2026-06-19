# using sort method

def sec_lar(l):
    l.sort()
    return l[-2]

l=[1,2,6,7,8,9,10,4,31,3,3]
print(sec_lar(l))


# using set method

'''def sec_lar(l):
    l=set(l)
    l.remove(max(l))
    return max(l)

l=[1,2,6,7,8,9,10,4,31,3,3]
print(sec_lar(l))'''


# using loop

def sec_lar(l):
    lar=l[0]
    sec_lar=l[0]
    for i in l:
        if i>lar:
            lar=i
    for i in l:
        if i>sec_lar and i<lar:
            sec_lar=i
    return sec_lar

# l=[1,2,6,7,8,19,10,4,31,3,3]
l= list(map(int, input().split()))
print(sec_lar(l))     





# l=[1,2,3,4,5,6]
# l1=[]
# for i in range(0,len(l),2):
#     l1.append(l[i:i+2])
    
# print(l1)



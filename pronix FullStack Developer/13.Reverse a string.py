'''
# using reverse index
a='abcd'
n=len(a)
ans=''
for i in range(n-1,-1,-1):
    ans+=a[i]
print(ans)

'''
#list compression

# l=[5,8,9,1,0,6,3]
# li=[l[i] for i in range((len(l))-1,-1,-1)]
# print(li)


# extra list
'''
l=[5,8,9,1,0,6]
li=[]
for i in range(len(l)-1,-1,-1):
    li.append(l[i])
print(li)

'''

#slicing

# l=[5,8,9,1,0,6]
# print(l[::-1])



# i/p:[5,8,9,1,0,6,3]
# o/p:[6,0,1,9,8,5]




# def reverse(l):
#     return l[::-1]

# l=[5,8,9,1,0,6]
# print(reverse(l))   


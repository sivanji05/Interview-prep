#prime number

'''n= 7
flag =0
if n>1:
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
if flag == 1:
    print("not prime")
else:
    print("prime")'''


#factorical
'''n=5
fact =1 
for i in range(1, n+1):
    fact*=i
print(fact)


def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)

n=5
print(fac(n))

'''


#fibonacci

# n=5
# n1=0
# n2 =1
# print("feb :", n1, n2, end=' ')
# for i in range(2, n):
#     n3 = n1+n2
#     n1 = n2
#     n2 = n3
#     print(n3, end = ' ')


# feb using recursion
'''
def feb(n):
    if n<=1:
        return n
    return feb(n-1)+feb(n-2)

n=5
for i in range(n):
    print(feb(i), end = " ")
'''

# string revese 
'''
s= "sivanji"
print(s[::-1])
'''
'''
s= "sivanji"
s1 = ''
for i in s:
    s1 =i+s1
print(s1)
'''

# using two points
'''
def rev(s):
    s= list(s)

    left, right= 0, len(s)-1

    while left<right:
    
        s[left], s[right]= s[right], s[left]
        left+=1
        right-=1
    return  ''.join(s)

s="sivanji"
print(rev(s))

'''
'''
def rev_l(l):
    return l[::-1]

l=[1,2,3,4,5]
print(rev_l(l))

'''
# reverse list
'''
def rev(l):
    l1=[]
    for i in range(len(l)-1,-1,-1):
        l1.append(l[i])
    return l1

l=[1,2,3,4,5]
print(rev(l))
'''

# reverse a list using two pointers
'''
def rev_l(l):

    left, right= 0, len(l)-1

    while left<right:

        l[left], l[right]=l[right],l[left]

    return l

l=[1,2,3,4,5]
print(rev_l(l))
'''

#palindrome
'''
s= "madam"
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")
'''

'''
def pal(s):

    i,j =0, len(s)-1

    while i<j:
        if s[i]!=s[j]:
            return "Not pal"
        else :
            i+=1
            j-=1
        return ("pal")
    
s="sivanji"
print(pal(s))
'''


# move the zeros to end
'''
def move(l):
    j=0
    for i in range(len(l)):
        if l[i]!=0:
            l[i],l[j]=l[j],l[i] 
            j+=1
    return l

l=[2,0,1,0,3,4]
print(move(l))
'''

# sort the list
'''
def sort_l(l):
    l.sort()

    return l 

l=[34,65,23,25,45,87,9]
print(sort_l(l))
'''
'''

def sort_li(l):
    n= len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]= l[j+1], l[j]

    return l

l= [2,5,8,3,6,7,3,1]
print(sort_li(l))

'''


#add two numbers
'''
def add_num(l1,l2):
    return l1+l2

l1,l2=2,4
print(add_num(l1,l2))

#add without + opertor

def add_num(a,b):
    while b!=0:
        carry= a&b
        a=a^b
        b= carry<<1
    return a
a,b=2,3
print(add_num(a,b))
'''

#max number in list
'''
def max_num(l):
    return max(l)

l=[5,3,4,6,9,8]
print(max_num(l))


def max_number(l):
    # max_n=float("-inf")
    max_n=l[0]
    for i in l:
        if i>max_n:
            max_n=i

    return max_n
l=[5,3,4,6,-9,8]
print(max_number(l))
'''


# num is even or odd
'''
n= 6
if (n&1) ==0:
    print("even")
else:
    print("odd")
'''

# no repeating number
'''
num = [2, 3, 4, 5, 3, 4, 2, 1]
d= {}
for i in num:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    if d[i]==1:
        print(i)
'''



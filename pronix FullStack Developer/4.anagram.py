# using sorted method

'''n1="Listen"
n2="Silent"

st1=sorted(n1.lower())
st2=sorted(n2.lower())

if st1==st2:
    print("Anagram")
else:
    print("Not Anagram")
    
'''



# counter

# from collections import Counter
# def check(s1,s2):
#     if Counter(s1)==Counter(s2):
#         print( "Anagram")
#     else:
#         print("Not Anagram")

# s1="Listen"
# s2="Silent"
# check(s1.lower(),s2.lower())



# using loop and dictionary
'''
def check(s1,s2):

    if len(s1)!=len(s2):
        return "Not Anagram"
    dict1={}
    dict2={}
    for i in s1:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    for i in s2:
        if i in dict2:
            dict2[i]+=1
        else:
            dict2[i]=1

    if dict1==dict2:
        return "Anagram"
    else:
        return "Not Anagram"
    
s1="Listen"
s2="Silent"
print(check(s1.lower(),s2.lower()))

'''
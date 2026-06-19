# using counter method
'''
from collections import Counter
def count_frq(list):
    counter=Counter(list)
    return counter

list=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,1,2,3,4,1,2,3,1,2,1]
c=count_frq(list)

for i in c:
    print(i,':',c[i])
    
'''

# using loop and dictionary

def count_frq(list):
    dict={}
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict

list=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8]
c=count_frq(list)
#print(c)
for i in c:
    print(i,':',c[i])

# max_ele=None
# max_value=0
# for key,value in c.items():
#     if value > max_value:
#         max_value=value
#         max_ele=key

# print('max element:',max_ele)
# print('max value:',max_value)

    
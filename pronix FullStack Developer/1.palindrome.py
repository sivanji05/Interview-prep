# using reverse indixing

# s='sivanji'
# n=s
# rev=''
# for i in range(len(n)-1,-1,-1):
#     rev+=n[i]
# print(rev)

# if s==rev:
#     print("palindrome")
# else:
#     print("not palindrome")



# without inbuilt funtion

def rev(s):
    revs_s=''
    for char in s:
        revs_s=char+revs_s
    # return revs_s
    if revs_s==s:
        return True
    else:
        return False

s=input("enter the string:")
revs=rev(s) 
print(revs)





# s="jahnavi"
# if s==s[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")





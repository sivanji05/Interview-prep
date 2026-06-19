#find 1st non-repeating character in a string
# s="aabbcddxvuqfdnfdkfksdlfen"
# for i in s:
#     if s.count(i)==1:
#         print(i)



# num=[2,3,4,5,3,4,2,1]
# for i in num:
#     if num.count(i)==2:
#         print(i)
        


num = [2, 3, 4, 5, 3, 4, 2, 1]
freq = {}
for i in num:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for i in num:
    if freq[i] == 1:
        print(i)
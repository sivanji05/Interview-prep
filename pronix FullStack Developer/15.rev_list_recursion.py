def reverse_lsit(l):
    
    if len(l)<=1:
        return l
    return [l[-1]]+reverse_lsit(l[:-1])

print(reverse_lsit([1,2,3,4,5]))
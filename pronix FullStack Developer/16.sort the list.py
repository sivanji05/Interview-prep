# l= [2,4,3,5,8,6,7]
# l.sort()
# print(l)

def bubble_sort(l):
    n=len(l)
    for i in range(n):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l


l= [2,4,3,5,8,6,7]
print(bubble_sort(l))


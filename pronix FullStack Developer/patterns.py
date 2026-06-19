
n=5
for i in range(n):
    for j in range(n):
        print("*",end='')
        if j!=n-1:
            print('-',end='')
    print()



# arrow head
"""
*
**
***
****
*****
****
***
**
*
"""
'''
n=int(input("enter the number:"))
for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print()
for i in range(n):
    for j in range(n-1-i):
        print("*",end='')
    print()

'''

# rambus
'''
    * 
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''
n=5
for i in range(n-1):
    for j in range(n-i):
        print(" ",end='')
    for k in range(i+1):
        print("*",end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end='')
    for k in range(n-i):
        print("*",end=" ")
    print()  

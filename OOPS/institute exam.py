# palindrome
# name='sas'
# temp=name
# r=temp.reversed()
# if r== name:
#     print(True)


# factorial


# def fact(n):
#   fact=1
#   for i in range(1,n+1):
#       fact*=i
#   return fact

# n=4
# print(fact(n))


#ele appears


# def ele_appears(n,k):
#     count=0
#     for i in n:
#       if i==k:
#          count+=1
#     return count

# n=[2,4,3,6,2,5,3,5,2,7]
# k=2
# s=ele_appears(n,k)
# print(s)
        

#largest ele

# def find_lar(num):
#     max_ele=0
#     for i in num:
#         if i>max_ele:
#             max_ele=i
#     return max_ele

# num=[2,4,7,6,9,4,3]
# print(find_lar(num))     


#reverse a string

# def reverse_string(s):
#     return s[::-1]

# s="sivanji"
# print(reverse_string(s))


# def reverse_string(s):
#     t=''
#     for i in range(len(s)-1, -1, -1):
#         t += s[i]
#     return t

# s='sivanji'
# print(reverse_string(s))



# palindrome

# def check_palindrome(s):
#   temp=name
#   t=''
#   for i in range(len(temp)-1,-1,-1):
#       t+=temp[i]
#   if t == name:
#       return "Is Palindrome"
#   return "Not Palindrome"

# name='saas'
# print(check_palindrome(name))



#How do we interact with the database in Django? Can you give an example.
# import sql.connector

# mydb = sql.connector.connect(
# 	host="localhost",
# 	user="yourusername",
# 	password="yourpassword",
# 	database="yourdatabase"
# )

#What is the role of Django’s urls.py and write an example on how do you link urls?

# # urls.py is a Python file that is used to define the URL patterns for a Django application.url's maintains the main role in django. we can access all views by using url's only , Every view must be map in url's file . In django we have url's file we map the all views in that file after import views file.

# example:
# from views  import my_view

# # map the view
# path("my_view/",my_view),

#Can you explain the concept of the DOM (Document Object Model) and how JavaScript interacts with it?
#The Document Object Model (DOM) is a programming interface for HTML and XML documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects. That way, programming languages can connect to the page.



#Can you explain the concept of branching in Git with an example?



# // JavaScript form validation

# function validateForm() {
#     var name = document.forms["myForm"]["name"].value;
#     var email = document.forms["myForm"]["email"].value;
#     var message = document.forms["myForm"]["message"].value;

#     if (name == "") {
#         alert("Name must be filled out");
#         return false;
#     }
#     if (email == "") {
#         alert("Email must be filled out");
#         return false;
#     }
#     if (message == "") {
#         alert("Message must be filled out");
#         return false;
#     }
#     return true;
# }

# // HTML form example
# /*
# <form name="myForm" onsubmit="return validateForm()" method="post">
#   Name: <input type="text" name="name"><br>
#   Email: <input type="text" name="email"><br>
#   Message: <textarea name="message"></textarea><br>
#   <input type="submit" value="Submit">
# </form>
# */
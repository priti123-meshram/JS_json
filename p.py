# a=4/5
# b=5//4
# print(a*b)






# import os.path
# import json
# print(("welcome to login signup"))
# user=input("you wants to login or signup:")
# file_exists=os.path.exists("text.json")
# if user=="signup":
#     user1=input("enter user name")
#     pass1=input("enter password")
#     pass2=input("enter your confirm password")
#     if pass1==pass2:
#         print("your password is confirmed")
#         birth=input("enter birthdate")
#         contactno=int(input("enter number"))
#         gender=input("enter the gender f/m")
#         hobbies=input("enter your hobbies")
#         qualification=input("enter your qualification")
#         dict={"username":user1,"pass2":pass2,"birth":birth,"contactno":contactno,"gender":gender,"hobbies":hobbies,"qualification":qualification}
#         if file_exists==True:
#             with open("text.json","r") as file:
#                 f=file.read()
#                 p=json.loads(f)
#                 p.append(dict)
#             with open("text.json","w") as d:
#                 json.dump(p,d,indent=2)
#         else:
#             with open("text.json","w") as d:
#                 json.dump([dict],d,indent=2)

#     else:
#         print("wrong password")
# else:
#     if user=="login":
#         usr_name=input("enter the usr_name:-")
#         if file_exists==True:
#             password=input("enter usr password:-")
#             with open("text.json","r")as file:
#                 a=file.read()
#                 d=json.loads(a)
#                 for i in range(len(d)):
#                     if d[i]["username"]==usr_name:
#                         if d[i]["pass2"]==password:
#                             print("login successful")
#                         else:
#                             print("wrong password")
#                     elif i == len(d)-1 and d[i]["username"]!=usr_name:
#                         print("Wrong ID")

#         else:
#             print("Wrong details")
#     print(d)











# def add():
#     a=int(input("enter the num"))
#     c=0
#     i=0
#     while i <a:
#         i=i+1
#         c=c+1
#         print(c,end="")
# add()






# n=[1,3,0,0,5,0,6,0,8,0]
# a=[]
# b=[]
# i=0
# while i<len(n):
#     if n[i]>0:
#         a.append(n[i])
#     else:
#         b.append(n[i])
#     i=i+1
# print(a)
# print(b)






# n=int(input("enter the num"))
# m=int(input("enter the num"))
# i=2
# while i <=m:
#     j=1
#     while j<=10:
#         a=i*j
#         print(a,end="  ")
#         # print(a)
#         j=j+1
#     print()
#     i=i+1



    
# t=float(input("enter the time"))
# if t>6 and t<=7:
#     print("exercies")
# elif t>7 or t<=9:
#     print("break fast")
# elif t>9 or t<=12.30:
#     print("coading")
# elif t>12.30 or t<=2:
#     print("break") 
# elif t>2 or t<=4:
#     print("coading")
# elif t>4 or t<=5:
#     print("culctural activity")
# elif t>5 or t<=5.30:
#     print("break")
# elif t>5.30 or t<=8:
#     print("coading")
# elif t>8 or t<=9:
#     print("english activity")
# else:
#     print("sleeping")
                                                          
                        

n=int(input("enter the num"))
if n%3==0 and n%7==0:
    print("Nav")
elif n%3==0:
    print("NavGurukul")
elif n%7==0:
    print("Gurukul")


# marks=30
# if(marks>=60):
#     print("A")
# elif(marks>=50):
#     print("B")
# elif(marks>=40):
#     print("C")
# else:
#     print("fail")

#     average_marks=int(input("enter marks:"))
#     if(average_marks>=70):
#         print("A")
#     elif(average_marks>=60 and average_marks<70):
#         print("B")
#     elif(average_marks>=50 and average_marks<60):
#         print("C")
#     elif(average_marks>=40 and average_marks<50):
#         print("D")
#     else:
#         print("E")

# # Take three inputs from a user, separately. Print the largest of the numbers.
# #     Hint: Determine what type of data is taken in as input

# input1=int(input("enter input1:"))
# input2=int(input("enter input2:"))
# input3=int(input("enter input3:"))
# if(input1>input2 and input1>input3):
#             print("f{input1} is the largest")
# elif(input2>input1 and input2>input3):
#             print("f{input2} is the largest")
# else:
#            print("f{input3} is the largest")


# # Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”, otherwise display “Normal temperature”

temp=int(input("enter temp:"))
if(temp>30):
     print("the temperature is too high")
elif(temp<15.5):
      print("the temperature is too low")
else:
      print("normal temperature")
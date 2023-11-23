# n="10"
# for i in n:
#     print(i)

#     y=range(0,1000)
#     for i in y:
#         print(i)

# # looping through a list
# sep_intake=["lilian","dennis","jace","bilal","tosh","tony"]
# for i in sep_intake:
#     print(i)

#     # loopin through a conditional statement
#     for i in range(20):
#         if i==5:
#             break
#         print(i)

#     for i in range(20):
#         if i==5:
#             continue
#         print(i)

#         # looping through a dictionary
#     person={"name" :"lilian kimanzi",
#              "age":30,
#              "location":"nairobi",
#              "email":"kimanzililian6@gmail.com",
#         }
#     for key,value in person.items():
#             print(key,value)

 # Write a program that displays a numbers 1 to 50 inside a list.
numbers= []
for i in range(1,51):
 numbers.append(i)
print(numbers)

    #  From 1 above display the ones divisible by 7 or 5 inside a list
numbers=[]
for i in range(1,51):
 if(i%7==0) or (i%5==0):
  numbers.append(i)
print(f"{numbers} numbers")

# Find sum and average of values in the range between 10 to 40.
values=[]
for i in range(10,41):
 values.append(i)
print(values)
sumation=sum(values)
average=sumation/len(values)
print(f"{sumation}sum")
print(f"{average}average")

# Put in a list the first 10 odd numbers between 10 to 50. 
odd_numbers=[]
for i in range(10,51):
     if(i%2!=0):
      odd_numbers.append(i)
      if len(odd_numbers)==10:
       break
print(f"{odd_numbers}odd_numbers")
  



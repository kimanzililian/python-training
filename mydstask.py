# my_ds = [23, “Jane”, (560), [“Lesson”, “Maths”, {“currency” : “KES”}], 987, (76,”John”)]
my_ds=[23, "Jane", (560), ["lesson", "maths", {"currency" : "KES"}], 987, (76, "John")]
# PRINT KES
print(my_ds[3][2]["currency"])
# print 560
print(my_ds[2])
# print maths
print(my_ds[3][1])
#  In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3][2]["amount"]=90
print(my_ds)
# Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#      Hint: Strings can be reversed using [::]
my_ds[4]=str(my_ds[4])
print(my_ds[4][2::-1])
#  Change the name “John” to “Jane
my_ds[5]=list(my_ds[5])
my_ds[5][1]="jane"
my_ds[5]=tuple(my_ds[5])
print(my_ds)

trainees = ["John", [2, ["James","Mary"]]]
# Display 2 from the list.
print(trainees[1][0])

#  Output James  from the list.
print(trainees[1][1][0])

#  Using a method add 56 at the end of the list.
trainees.append(56)
print(trainees)

# Using a method add the name Mike between James and Mary
trainees.insert(2,"mike")
print(trainees)

# Change the value of 2 to 8
trainees=[1][0]=8
print(trainees)

# Remove John and Mary from the list.
trainees = ["John", [2, ["James","Mary"]]]
del(trainees)
print(trainees)


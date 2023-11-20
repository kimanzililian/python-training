# creating dictionaries
person={"name" :"lilian kimanzi",
       "age":30,
       "location":"nairobi",
       "email":"kimanzililian6@gmail.com",
        }
# access this values in a dictionary
print(person["age"])
print(person["location"])
# updating values in a dictionaries
person["age"]=40
person["name"]="jace omari"
person["location"]="mwingi"
print(person)
# adding a new key value pair
person["gender"]="male"
person["address"]="0010-43709"

print(person)

# dictionary methods

print(person.get("age"))
new_data={
    "course":"fashion design","campus":"UOE"
}
person.update(new_data)

print(person)
person.pop("age")
print(person)

print(person.copy())
print(person.items())
print(person.popitem())
print(len(person))
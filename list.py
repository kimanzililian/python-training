person=["lilian kimanzi",20,"female","nairobi","0703186948"]
print(person[-1])

days_of_week=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print(days_of_week.index("wednesday"))
print(days_of_week[2])

group_list=[[1,2,3,4,5],"monday","tuesday"]
print(group_list[1][-1])
print(len(group_list))

add_list=days_of_week + group_list
print(add_list)
print("monday" in days_of_week)
print("friday" not in group_list)

group_list=[[1,2,3,4,5],"monday","tuesday"]
group_list[-1]= "friday"
print(group_list)

group_list=[[1,2,3,4,5],"monday","tuesday"]
group_list.append("friday")
print(group_list)

group_list=[[1,2,3,4,5],"monday","tuesday"]
group_list.pop()
print(group_list)

group_list=[[1,2,3,4,5],"monday","tuesday"]
group_list.clear()
print(group_list)

group_list=[[1,2,3,4,5],"monday","tuesday"]
group_list.insert(2,"lilian")
print(group_list)
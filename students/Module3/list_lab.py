#----------------------------------------#
# Title: list_lab.py
# Initial File
# Claire Yoon,2019-01-27,New file
#----------------------------------------#

#Series 1

lst = ["Apples", "Pears", "Oranges","Peaches"]
print(lst)
fruit1 = input("Type another fruit that you want to add: ")
lst.append(fruit1)
print(lst)
numb = input("Type a number that you want to check: ")
print("You typed",numb, ", and corresponding fruit is",lst[int(numb)-1])

fruit2 = input("Type another fruit that you want to add: ")
temp = [fruit2]
lst = temp + lst
print(lst)

fruit3 = input("Type another fruit that you want to add: ")
lst.insert(0,fruit3)
print(lst)

for i in range(len(lst)):
    if lst[i][:1].lower() == 'p':
        print(lst[i])

#Series 2
lst2 = lst
print(lst2)
lst2 = lst2[:-1]
print(lst2)

fruit4 = input("Type a fruit that you want to delete: ")
temp2 = []
for i in range(len(lst2)):
    if fruit4.lower() != lst2[i].lower():
        temp2.append(lst2[i])
lst2 = temp2
print(lst2)

#bonus
# lst2 = lst2 + lst2
# temp2 = []
# for i in range(len(lst2)):
#     if fruit4.lower() != lst2[i].lower():
#         temp2.append(lst2[i])
# lst2 = temp2
# print(lst2)


#Series 3
lst3 = lst

newlst = []
for i in range(len(lst3)):
    ans = input("Do you like "+lst3[i]+"? :")
    if ans.lower() == 'yes':
        newlst.append(lst3[i])
    elif ans.lower() == 'no':
        pass
    else:
        print('Please use valid answer (yes/no)')

lst3 = newlst
print(lst3)


#Series 4
lst4 = lst

lst4cp = []
for i in range(len(lst4)):
    lst4cp.append(lst4[i][::-1])

lst = lst[:-1]
print(lst)

print(lst4cp)

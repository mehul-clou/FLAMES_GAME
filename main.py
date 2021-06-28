name1=input("enter the name 1 ").lower()
name2=input("enter the name 2 ").lower()

#replace the whitespace with the empty string
name1= name1.replace(" ","",1)
name2=name2.replace(" ","")
print(name1)
print(name2)

for i in name1:
    if i in name2:
        name1 = name1.replace(i,"",1)
        name2 = name2.replace(i,"",1)
# print(name1)
# print(name2)
count = len(name1+name2)
print(count)

if count>0:
    list1 = ["F", "L", "A", "M", "E", "S"]
    while len(list1)>1:
        c = count%len(list1)
        s_index = c-1
        if s_index>=0:
            left = list1[:s_index]
            right = list1[s_index+1:]
            list1 = right+left
        else:
            list1=list1[:len(list1)-1]
    print("Relationship is ",list1[0])
else:
    print("Enter different names")
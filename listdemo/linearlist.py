lst1=[10,11,12,13,14]
lst2=[11,14,15,16,17]
dup_lst=list()


for num in lst1:
    if num in lst2:
        dup_lst.append(num)
print(dup_lst)
# lst=[10,11,11,1,13,14,14,14]
#print most frequent element from the list 14
# print first recursive number
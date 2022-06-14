# lst=[10,10,1,12,13,14,15,16,16,16]
# st=set(lst)
# print(st)


# st1={1,2,3,4,5}
# st2={10,11,12,2,3}
# union_set=st1.union(st2)
# print(union_set)
#
# intersection_set=st1.intersection(st2)
# print(intersection_set)
#
# diff_set=st1.difference(st2)
# print(diff_set)

students=["ram","ravi","hari","tom","nikil","jain","john"]
passed_students=["ravi","hari","tom"]
# st_students=set(students)
# st_passed=set(passed_students)
# failed=st_students-(st_passed)
# print(failed)
fail_st=set(students).difference(set(passed_students))
print(fail_st)


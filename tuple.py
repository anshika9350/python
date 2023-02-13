#mutable
# list_1 = [1,2,3,4]
# list_2 = list_1
# print(list_1)
# print(list_2)

#immutable
tuple_1 = (1,2,2,3)
tuple_2 = tuple_1
tuple_1[4] = 7
print(tuple_1)
print(tuple_2)
#it throws an error because tuple does not update the items while list can do this task
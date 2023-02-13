set_1 = {'name' : 'john','age': 13,'courses':['math','physics']}
print(set_1['name'])  #prints the john
print(set_1.get('courses'))  #prints the courses
print(set_1.get('ab','not found!'))  #prints the massege not found!
set_1['id']=50   #id key is added to the set
print(set_1)
print(set_1.keys())  #shows the keys
print(set_1.values()) #shows the values
print(set_1.items())  #shows keys and values
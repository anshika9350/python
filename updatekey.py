set_1 = {'name' : 'john','age': 13,'courses':['math','physics']}
set_1['name']= 'anshika'  #update the name jon to anshika
print(set_1)
#optimized method for updation by using update
set_1.update({'age': 56,'courses': ['data','gk']})  #update the set in a single line
print(set_1)
set_1.pop('age')
print(set_1)
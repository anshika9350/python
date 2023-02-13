items = [1,'anshi',34,111]
for item in items: #we can name that item whatever we want
    print(item)
for inde,item in enumerate(items): #returns the index and items in list
    print(inde,item)
 # we can start our index from wherever we want by setting the start value
for index,item in enumerate(items,start=1  ):
    print(index,item)
 
courses = ['hindi','english','maths','history']
print(len(courses)) #prints the length of the array
print(courses[0]) #print the string at 0 index
print(courses[-1]) #prints the last string in aaray
print(courses[:2]) #starts with 0 and end on 1
print(courses[2:]) #starts with 2 and end on 3

courses_1 = ['science','biology']
courses.append('physics') #add the item at last of the list
print(courses)
courses.extend('chemistry') #takes each individual item like c h e m i s t r y
print(courses)
courses.extend(courses_1)
print(courses)
courses.insert(0,'art') #just add the art at index 0 and shifted the list
courses.remove('c') #remove the item
print(courses)
























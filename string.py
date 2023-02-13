#printing string
message = 'hello world'
print(message)

#length of string
print(len(message))

#replace the string
new_message = message.replace('world','anshika')
print(new_message)

#count the character
print(new_message.count('e'))
#count the string
print(new_message.count('hello'))

#printing particular character of string
print(message[4])

#uppercase and lowercase the string
print(message.upper())
print(message.lower())

#concatination of string
greeting = 'hi'
name = 'anshika'
page ='{},{}'.format(greeting,name)
print(page)
#another way of concatination
new_page = f'{greeting} {name}'
print(new_page)

#find the string
print(message.find('hello'))

#slicing
print(message[:5])
print(message[5:7])
print(message[5:])
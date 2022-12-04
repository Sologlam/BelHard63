message = ('Alex', 40, 'Minsk')
name = message[0]
age = str(message[1])
city = message[2]
print(f'Hello {name} ! Your age is {age}, and you are from {city} !')
print("Hello %s ! Your age is %s, and you are from %s !" % (name, age, city))
print("Hello {} ! Your age is {}, and you are from {} !".format(name, age, city))

a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)

Hello_Vlad = 'Hello Vlad!'
print(Hello_Vlad)
print(Hello_Vlad[::-1])

#print(Hello_python[::-1])
Hello_python = 'Hello python!'
a = 5
if a % 2 == 0:
    print(Hello_python[::-1])
else:
    print(Hello_python.upper())

Hello_skeem = 'Hello Skeemans Church'
if 1 > 0:
    print(Hello_skeem)
else:

    print(Hello_skeem.upper())

x, y = 200, 700
if x > y:
    print('x bigger y')
elif x == y:
    print('x equals y')
elif x < y and 600 > 800:
    print('right')
else:
    print('x smaller y')

my_text = 'Misha had 10 apples and he gave 3 to Tolik, how many apples did Misha have?'
my_text1 = 'Misha had 5 appales'
my_text2 = 'Misha had 8 appales'
my_text3 = 'Misha had 7 appales'
#my_text = my_text3
if my_text == my_text3:
    print('Misha had 7 appales')
elif my_text == my_text2:
    print('Misha had 8 appales')
elif my_text == my_text1:
    print('Misha had 5 appales')
else:
    print('Misha had 7 appales')

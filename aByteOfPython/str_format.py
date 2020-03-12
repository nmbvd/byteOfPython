age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

print('{} was {} years old when he wrote this book'.format("name", "age"))
print('Why is {} playing with that python?'.format(name))

print('{name} was {age} years old when he wrote this book'.format(name=name, age=age))
print('Why is {name} playing with that python?'.format(name=name))

print(f'{name} was {age} years old when he wrote this book')  # notice the 'f' before the string
print(f'Why is {name} playing with that python?')  # notice the 'f' before the string

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}+{1:.6f}'.format(1.0/3,3.1/45))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^7}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

print('a', end='')
print('b')

print("test\ttest")
print(r"Newlines are indicated by \n")


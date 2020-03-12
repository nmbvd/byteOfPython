def func1(d,e,a=1,b=2,c=3):
    print(d,e,a,b,c)
func1(34,45,67)
func1(d=23,e=34,c=35)

def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)

def total(a=5, *numbers, **phonebook):
    print('a', a)

    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    #iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)


total(10,1,2,3,Jack=1123,John=2231,Inge=1560)

def swap(x,y):
    buffer=x
    x=y
    y=buffer
    return (x,y)

a=1
b=2
(a,b)=swap(a,b)
print(a,b)
max(3,4)
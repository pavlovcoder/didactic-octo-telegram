x = 10
y = 12

# Output: x > y is False
print('x > y  is',x>y)

# Output: x < y is True
print('x < y  is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)

'''
> 	Greater that - True if left operand is greater than the right 	x > y
< 	Less that - True if left operand is less than the right 	x < y
== 	Equal to - True if both operands are equal 	x == y
!= 	Not equal to - True if operands are not equal 	x != y
>= 	Greater than or equal to - True if left operand is greater than or equal to the right 	x >= y
<= 	Less than or equal to - True if left operand is less than or equal to the right
'''

year = 2016
event = 'Referendum'
f'Results of the {year} {event}'

def f(x):
    return {
        'a': 1,
        'b': 2,
    }[x]

    x if C else y
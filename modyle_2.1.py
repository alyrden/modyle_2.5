first = input('Ведите 1-е число: ')
second = input('Ведите 2-е число: ')
third = input('Ведите 3-е число: ')
a = bool(first == second)
b = bool(first == third)
c = bool(second == third)
if a and not c:
    st_ = first + second
    print(2)
elif c and not a:
    stt_ = first + third
    print(2)
elif b and not c:
    sttt_ = second + third
    print(2)
elif not a and not b and not c:
    sq_ = 0
    print(sq_)
else:
    a and b and c
    sqw_ = first + second + third
    print(3)
    
# использованны все операторы
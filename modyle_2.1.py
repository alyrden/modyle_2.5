first = input('Ведите 1-е число: ')
second = input('Ведите 2-е число: ')
third = input('Ведите 3-е число: ')
a = bool(first == second)
b = bool(first == third)
c = bool(second == third)
if a and not c:
    st_ = first + second
    print('\n'.join(st_))
elif c and not a:
    stt_ = first + third
    print('\n'.join(stt_))
elif b and not c:
    sttt_ = second + third
    print('\n'.join(sttt_))
elif not a and not b and not c:
    sq_ = 0
    print(sq_)
elif a and b and c:
    sqw_ = first + second + third
    print('\n'.join(sqw_))


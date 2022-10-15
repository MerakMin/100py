C = int(input(), 16)
for i in range(0, 15):
    i += 1
    print('%X'%C, '*%X'%i, '=%X'%(C*i), sep='')
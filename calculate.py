from module import *

while True :
    print('Menu', '---------', '1: add', "2: sub", '3: multiply', '4: divide','5: stop', sep='\n')
    x = int(input(':'))
    if x == 1:
        a = int(input('num1 :'))
        b = int(input('num2 :'))
        print(add(a, b))
    elif x == 2:
        a = int(input('num1 :'))
        b = int(input('num2 :'))
        print(sub(a, b))
    elif x == 3:
        a = int(input('num1 :'))
        b = int(input('num2 :'))
        print(mul(a, b))
    elif x == 4:
        a = int(input('num1 :'))
        b = int(input('num2 :'))
        if b == 0:
            print('님 초등학교 안나오심..? 다시 하세요')
        else:
            print(div(a, b))
    elif x == 5:
        print('Have a good day!')
        break
    else :
        print('눈을 크게 뜨고 보이는 숫자중에 선택하세요')

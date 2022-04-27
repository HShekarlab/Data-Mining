print('  The Quadratic Equation of the Given Roots  ')
print(' Programmer: Mohammad Rajabpur; Nov. 30, 2019')
print('  ********* rajabpur.blogsky.com ********* \n')
print(' To exit the program, assign 0 to x1 & x2. \n')

while True:
    print('---------------------------------------\n')
    x1 = float(input(' x1 = '))
    x2 = float(input(' x2 = '))
    b = x1 + x2
    c = x1 * x2

    if b>0 and c>0:
        print(' X^2 - ', b, 'X + ', c, ' = 0 \n')
    elif b>0 and c<0:
        print(' X^2 - ', b, 'X ', c, ' = 0 \n')
    elif b>0 and c==0:
        print(' X^2 - ', b, 'X = 0 \n')
    elif b<0 and c>0:
        print(' X^2 + ', -b, 'X + ', c, ' = 0 \n')
    elif b<0 and c<0:
        print(' X^2 + ', -b, 'X ', c, ' = 0 \n')
    elif b<0 and c==0:
        print(' X^2 + ', -b, 'X = 0 \n')
    elif b==0 and c<0:
        print(' X^2 ', c, ' = 0 \n')
    elif b==0 and c==0:
        print(' X^2 = 0')
        print(' The program is terminated. \n')
        break




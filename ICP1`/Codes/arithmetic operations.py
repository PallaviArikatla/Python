num1 = input('enter first number:')
num2 = input('enter second number:')
try:
    fNum = int(num1)
    sNum = int(num2)
    print('sum is:' + str(fNum+sNum))
except ValueError:
    print('please enter an integer')



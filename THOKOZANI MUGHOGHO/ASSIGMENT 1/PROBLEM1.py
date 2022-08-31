def add():
    print('Addition')
    print ('Enter First Number')
    x = input()
    print ('Enter Second Number')
    y = input()
    number1 = int(x)
    number2 = int(y)
    sum = number1 + number2
    print('Solution:', number1, ' + ', number2, ' is ', sum)
    print('enter any number greater than 0 then enter to restart the program or 0 to exit')
    next = input()
    nxt = int(next)
    if (nxt == 0):
        print('finished processing')
    elif (nxt > 0):
        main()

def sub():
    print('Subtraction')
    print ('Enter First Number')
    x = input()
    print ('Enter Second Number')
    y = input()
    number1 = int(x)
    number2 = int(y)
    sum = number1 - number2
    print('Solution:', number1, ' - ', number2, ' is ', sum)
    print('enter any number greater than 0 then enter to restart the program or 0 to exit')
    next = input()
    nxt = int(next)
    if (nxt == 0):
        print('finished processing')
    elif (nxt > 0):
        main()

def product():
    print('Product')
    print ('Enter First Number')
    x = input()
    print ('Enter Second Number')
    y = input()
    number1 = int(x)
    number2 = int(y)
    sum = number1 * number2
    print('Solution:', number1, ' X ', number2, ' is ', sum)
    print('enter any number greater than 0 then enter to restart the program or 0 to exit')
    next = input()
    nxt = int(next)
    if (nxt == 0):
        print('finished processing')
    elif (nxt > 0):
        main()

def division():
    print('Division')
    print ('Enter First Number')
    x = input()
    print ('Enter Second Number')
    y = input()
    number1 = int(x)
    number2 = int(y)
    sum = number1 / number2
    print('Solution:', number1, ' / ', number2, ' is ', sum)
    print('enter any number greater than 0 then enter to restart the program or 0 to exit')
    next = input()
    nxt = int(next)
    if (nxt == 0):
        print('finished processing')
    elif (nxt > 0):
        main()

def main():
    print('Welcomee to calculator simulator')
    print('Python Fundamentals Individual assessment 1')
    print('Select an arithmetic operator that you want to use')
    print('Choose 1 for Addition')
    print('Choose 2 for Subtraction')
    print('Choose 3 for Multiplication')
    print('Choose 4 for Division')
    c = input()
    choice = int(c)
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        product()
    elif choice == 4:
        division()

main()
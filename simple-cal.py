print('select operations')
print('1.addition')
print('2.multiplication')
print('3.substraction')
print('4.division')
print('5.exponential')

if choice == input('Enter choice:')

num1 = input('Enter num1: ')
num2 = input('Enter num2: ')
num1 = int(num1)
num2 = int(num2)

add = str(num1 + num2)
multiply = str(num1 * num2)
substract = str(num1 - num2)
divide = str(num1 / num2)
exponent = str(num1 ** num2)

if choice == '1':
    print(add)
elif choice == '2':
    print(multiply)
elif choice == '3':
    print(substract)
elif choice == '4':
    print(divide)
else:
    print(exponent)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

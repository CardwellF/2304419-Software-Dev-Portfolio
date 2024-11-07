import math
from tabulate import tabulate
#calculations
'''basic calculations'''
def addition():
    a=int(input("enter a number: "))#input
    b=int(input("enter a number: "))#input
    print(f"the answer of {a} + {b} = ", a+b)#print answer showing calculation
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")#asks user if they want to continue
    if ret == "return":#if statement for ret variable
        main()#calls main function
    else:#anything else other than 'return'
        print("closing program, thanks for using")#thank you message
def subtraction():
    a=int(input("enter a number: "))#input
    b=int(input("enter a number: "))#input
    print(f"the answer of {a} - {b} = ", a-b)#print answer showing calculation
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")#asks user if they want to continue
    if ret == "return":#if statement for ret variable
        main()#calls main function
    else:#anything else other than 'return'
        print("closing program, thanks for using")#thank you message
def multiplication():
    try:#tries to run whats in it
        a=int(input("enter a number: "))#input
        b=int(input("enter a number: "))#input
        if a == 0 or b == 0:#if statement to check if 0 was input
            print("any number timed by 0 = 0, please select diiferent numbers")#warning message
            multiplication()#calls multiplication function
        else:#if statement dont meet condition
            print(f"the answer of {a} x {b} = ", a*b)#print calculation and solution
            ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")#asks user if they want to continue
            if ret == "return":#if statement for ret variable
                main()#calls main function
            else:#anything else other than 'return'
                print("closing program, thanks for using")#thank you message
    except ValueError:#error exceptence value error
        print("select digit values")#error message
        multiplication()#function loop
def division():
    try:
        a=int(input("enter a number: "))#input
        b=int(input("enter a number: "))#input
        if a == 0 or b == 0:#check value entering
            print("dividing by 0 not posible, please select diiferent numbers")#error
            division()#function loop
        else:#if statement dont meet condition
            print(f"the answer of {a} / {b} = ", a/b)#print calculation and solution
            ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")#asks user if they want to continue
            if ret == "return":#if statement for ret variable
                main()#calls main function
            else:#anything else other than 'return'
                print("closing program, thanks for using")#thank you message
    except ValueError:#error exceptence value error
        print("select digit values")#error message
        division()#function loop
'''advanced calculations'''
def exponential():
    a=int(input("enter a number in digit form: "))#input
    print(f"the exponent of {a} = ", math.exp(a))#print calculation and solution
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")#asks user if they want to continue
    if ret == "return":#if statement for ret variable
        main()#calls main function
    else:#if statement dont meet condition
        print("closing program, thanks for using")#thank you message
def square_root():
    a=int(input("enter a number in digit form"))#input
    print(f"the square root of {a} = ", math.sqrt(a))#print calculation and solution
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")#asks user if they want to continue
    if ret == "return":#if statement for ret variable
        main()#calls main function
    else:#if statement dont meet condition
        print("closing program, thanks for using")#thank you message
def log_base_ten():
    a=int(input("enter a number in digit form: "))#input
    print(f"the log of {a} in base 10 = ", math.log10(a))#print calculation and solution
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")#asks user if they want to continue
    if ret == "return":#if statement for ret variable
        main()#calls main function
    else:#if statement dont meet condition
        print("closing program, thanks for using")#thank you message
def natural_log():
    a=int(input("enter a number in digit form: "))#input
    print(f"the natural log of {a} = ", math.log(a))#print calculation and solution
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")#asks user if they want to continue
    if ret == "return":#if statement for ret variable
        main()#calls main function
    else:#if statement dont meet condition
        print("closing program, thanks for using")#thank you message
def sine():
    a=int(input("enter a number in digit form: "))#input
    print(f"the sine of {a} = ", math.sin(a))#print calculation and solution
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")#asks user if they want to continue
    if ret == "return":#if statement for ret variable
        main()#calls main function
    else:#if statement dont meet condition
        print("closing program, thanks for using")#thank you message
def cosine():
    a=int(input("enter a number in digit form: "))#input
    print(f"the cosine of {a} = ", math.cos(a))#print calculation and solution
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")#asks user if they want to continue
    if ret == "return":#if statement for ret variable
        main()#calls main function
    else:#if statement dont meet condition
        print("closing program, thanks for using")#thank you message
def tangent():
    a=int(input("enter a number in digit form: "))#input
    print(f"the tangent of {a} = ", math.tan(a))#print calculation and solution
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")#asks user if they want to continue
    if ret == "return":#if statement for ret variable
        main()#calls main function
    else:#if statement dont meet condition
        print("closing program, thanks for using")#thank you message

#main
def main():
    print("Scientific Calculator")#title
    #operation difficulty list
    operationLevel=[
        ["input", "selection"],
        ["bsc", "Basic Operations"],
        ["adv", "Advanced Operations"],
        ["ext", "exit"]
    ]
    inp=input(tabulate(operationLevel, headers="firstrow", tablefmt="fancy_grid"))#input with tabulate list
    #input == bsc (basic)
    if inp == "bsc":
        #operation list
        operations=[
            ["input", "selection"],
            ["ad", "Addition"],
            ["sb", "Subtraction"],
            ["mt", "Multiplication"],
            ["dv", "Division"],
            ["bk", "return"]
        ]
        ans=input(tabulate(operations, headers="firstrow", tablefmt="fancy_grid"))#input with tabulate list
        if ans == "ad":#ans = ad(add)
            addition()#call function
        elif ans == "sb":#ans = sb(sub)
            subtraction()#call function
        elif ans == "mt":#ans = mt(multiply)
            multiplication()#call function
        elif ans == "dv":#ans = dv(divde)
            division()#call function
        else:#any other input
            main()#call function
    elif inp == "adv":
        #operation list
        operations=[
            ["input", "selection"],
            ["ex", "exponential"],
            ["sr", "square root"],
            ["lg", "log base 10"],
            ["bl", "natural log"],
            ["sn", "sine"],
            ["cs", "cosine"],
            ["tn", "tangent"],
            ["bk", "return"]
        ]
        ans=input(tabulate(operations, headers="firstrow", tablefmt="fancy_grid"))#input with tabulate list
        if ans == "ex":#ans == ex(exponential)
            exponential()#call function
        elif ans == "sr":#ans == sr(square root)
            square_root()#call function
        elif ans == "lg":#ans == lg(log base 10)
            log_base_ten()#call function
        elif ans == "bl":#ans == bl(base log)
            natural_log()#call function
        elif ans == "sn":#ans == sn(sine
            sine()#call function
        elif ans == "cs":#ans == cs(cosine)
            cosine()#call function
        elif ans == "tn":#ans == tn(tangent
            tangent()#call function
        else:#any other input
            main()
if __name__ == "__main__": 
    main()#calls main function 

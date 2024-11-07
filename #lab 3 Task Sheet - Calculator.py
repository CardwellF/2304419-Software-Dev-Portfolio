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
        else:
            print(f"the answer of {a} x {b} = ", a*b)
            ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")
            if ret == "return":
                main()
            else:
                print("closing program, thanks for using")
    except ValueError:
        print("select digit values")
        multiplication()
def division():
    try:
        a=int(input("enter a number: "))
        b=int(input("enter a number: "))
        if a == 0 or b == 0:
            print("dividing by 0 not posible, please select diiferent numbers")
            division()
        else:
            print(f"the answer of {a} / {b} = ", a/b)
            ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")
            if ret == "return":
                main()
            else:
                print("closing program, thanks for using")
    except ValueError:
        print("select digit values")
        division()
'''advanced calculations'''
def exponential():
    a=int(input("enter a number in digit form: "))
    print(f"the exponent of {a} = ", math.exp(a))
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")
    if ret == "return":
        main()
    else:
        print("closing program, thanks for using")
def square_root():
    a=int(input("enter a number in digit form"))
    print(f"the square root of {a} = ", math.sqrt(a))
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")
    if ret == "return":
        main()
    else:
        print("closing program, thanks for using")
def log_base_ten():
    a=int(input("enter a number in digit form: "))
    print(f"the log of {a} in base 10 = ", math.log10(a))
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")
    if ret == "return":
        main()
    else:
        print("closing program, thanks for using")
def natural_log():
    a=int(input("enter a number in digit form: "))
    print(f"the natural log of {a} = ", math.log(a))
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")
    if ret == "return":
        main()
    else:
        print("closing program, thanks for using")
def sine():
    a=int(input("enter a number in digit form: "))
    print(f"the sine of {a} = ", math.sin(a))
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")
    if ret == "return":
        main()
    else:
        print("closing program, thanks for using")
def cosine():
    a=int(input("enter a number in digit form: "))
    print(f"the cosine of {a} = ", math.cos(a))
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")
    if ret == "return":
        main()
    else:
        print("closing program, thanks for using")
def tangent():
    a=int(input("enter a number in digit form: "))
    print(f"the tangent of {a} = ", math.tan(a))
    ret=input("please type 'return' to select another operation or type 'exit' to stop the program: ")
    if ret == "return":
        main()
    else:
        print("closing program, thanks for using")

#main
def main():
    print("Scientific Calculator")
    operationLevel=[
        ["input", "selection"],
        ["bsc", "Basic Operations"],
        ["adv", "Advanced Operations"],
        ["ext", "exit"]
    ]
    inp=input(tabulate(operationLevel, headers="firstrow", tablefmt="fancy_grid"))
    if inp == "bsc":
        operations=[
            ["input", "selection"],
            ["ad", "Addition"],
            ["sb", "Subtraction"],
            ["mt", "Multiplication"],
            ["dv", "Division"],
            ["bk", "return"]
        ]
        ans=input(tabulate(operations, headers="firstrow", tablefmt="fancy_grid"))
        if ans == "ad":
            addition()
        elif ans == "sb":
            subtraction()
        elif ans == "mt":
            multiplication()
        elif ans == "dv":
            division()
        else:
            main()
    elif inp == "adv":
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
        ans=input(tabulate(operations, headers="firstrow", tablefmt="fancy_grid"))
        if ans == "ex":
            exponential()
        elif ans == "sr":
            square_root()
        elif ans == "lg":
            log_base_ten()
        elif ans == "bl":
            natural_log()
        elif ans == "sn":
            sine()
        elif ans == "cs":
            cosine()
        elif ans == "tn":
            tangent()
main()   
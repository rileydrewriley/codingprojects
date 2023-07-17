import math

while True:
    print("\nChoose your math operation. \n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square Root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")
    
    oper = input("Your option from the menu: ")
   
    #Addition Function
    if oper == "0":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        
        print("\nThe result is " + str(val1 + val2) + "\n")
        
        back = input("\nGo back to the main menu? (y/n)")
        
        if back == "y":
            continue
        else:
            break
      
     #Subtraction Function 
    if oper == "1":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        
        if val1 >= val2:
            print("\nThe result is " + str(val1 - val2) + "\n")
        else:
            print("\nThe result is " + str(val2 - val1) + "\n")
        
        back = input("\nGo back to the main menu? (y/n)")
        
        if back == "y":
            continue
        else:
            break
     
    #Multiplication Function
    if oper == "2":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nMultiplied by: "))
        
        print("\nThe result is " + str(val1 * val2) + "\n")
        
        back = input("\nGo back to the main menu? (y/n)")
        
        if back == "y":
            continue
        else:
            break
        
    #Division Function
    if oper == "3":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nDivided by: "))
        
        print("\nThe result is " + str(val1 // val2) + "\n")
        
        back = input("\nGo back to the main menu? (y/n)")
        
        if back == "y":
            continue
        else:
            break
    
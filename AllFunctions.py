class allFunctions():
    def subFieldsList():
        subFields=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for field in subFields:
            print(field)
    
    def oddEven():
        num=int(input("Enter the number:"))
        if(num%2==1):
            print("Entered number is Odd")
            message="Odd number"
        else:
            print("Entered number is Even")
            message="Even number"
            return message
    
    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        EligibleForMarriage="ELIGIBLE"
        NotEligibleForMarriage="NOT ELIGIBLE"
        invalidAgeEntered="Invalid Age entered"
        if(gender=='Male'):
            if(age>=21):
                print(EligibleForMarriage)
            elif(age<21):
                print(NotEligibleForMarriage)
            else:
                print(invalidAgeEntered)
        elif(gender=='Female'):
            if(age>=18):
                print(EligibleForMarriage)
            elif(age<18):
                print(NotEligibleForMarriage)
            else:
                print(invalidAgeEntered)
        else:
            print("Invalid gender entered")
        
    def Percentage():
        Subject1=int(input("Enter subject 1 marks:"))
        Subject2=int(input("Enter subject 2 marks:"))
        Subject3=int(input("Enter subject 3 marks:"))
        Subject4=int(input("Enter subject 4 marks:"))
        Subject5=int(input("Enter subject 5 marks:"))
        total=Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total:",total)
        percentage=float(total/5)
        print("Percentage:",percentage)
        roundOffPercent=round(percentage,14)
        
    def triangle():    
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        # Area formula: (Height*Breadth)/2
        area = (height*breadth)/2
        print("Area of Triangle:", area)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        # Perimeter formula: Height1+Height2+Breadth
        perimeter=height1+height2+Breadth
        print("Perimeter of Triangle:", perimeter)
def chatbot():

    print("Hi there! I am Chatbot. To start, please enter your name.")

    name = input("First Name: ")

    print("Nice to meet you,", name, ". What is your year of birth in YYYY format?")

    def YOB():
        
        birthYearStr = input("Year of birth: ")

        birthYear = int(birthYearStr)
    
        if 1899 < birthYear < 1947:
            print("You are Pre-war Generation.")
        
        elif 1946 < birthYear < 1965:
           print("You are Baby Boomer.")     
            
        elif 1964 < birthYear < 1980:
            print("You are Generation X.")

        elif 1979 < birthYear<2000:
            print("You are Millennial.")

        elif 1999 < birthYear<2021:
            print("You are Generation Z.")

        else:
            print("Please enter a valid year of birth in YYYY format.")
            YOB()
    YOB()
chatbot()


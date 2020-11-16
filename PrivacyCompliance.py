from user import user
        
def chatbot():

    print("Hi there! I am Chatbot. To start, please enter your name.")

    name = input("First Name: ")

    print("Nice to meet you,", name, ". What is your year of birth in YYYY format?")

    def YOB():

        global birthYear
            
        while True:
            try:
                birthYear = int(input("Year of birth: "))
                break
            except:
                print("Please enter a valid year of birth in YYYY format.")
    
        if 1899 < birthYear < 1946:
            print("You are Pre-war Generation.")
        
        elif 1945 < birthYear < 1965:
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

        return

    YOB()
chatbot()            

questions = ["a) Average portions of fruit and veg per day: \n",
             "b) Years smoking: \n",
]

user_info = [
    user(questions[0]),
    user(questions[1])
]

age = 2020-birthYear
age_int = int(age)
user_input = [age_int]

print("\n\nIn the next section, you will be talking to Cancer Riskbot, who will help you from here.\n\n")

history = {}

questions = ["a) Average portions of fruit and veg per day: \n",
             "b) Years smoking: \n",
]

def cancer_riskbot_3():
    print("Hi, I'm Cancer Riskbot 3.0. In this latest version, I can inform you all the data I have collected from you. To use this feature, simply enter the following at any point in our converation:\nhistory\n\nYou are now ready to find out your cancer risk category")
    print("\n\nPlease answer the following, by entering data about yourself.\n\n")

    while True:
    
        for user in user_info:
            answer = input(user.prompt)
            
            if answer == "history":
                print("Data collected from this conversation:\n")
                for keys,values in history.items():
                    print(keys)
                    print(values)

                answer = input(user.prompt)
            user_input.append(int(answer))
            history[user.prompt] = answer
        
        if user_input[1] <= 2 and user_input[2] >= 5:
            print("Your cancer risk category is HIGH.")
        elif user_input[2] >= 5 and user_input[0] > 40:
            print("Your cancer risk category is HIGH.")
        elif user_input[0] > 40 and user_input[1] <= 2 and user_input[2] < 5:
            print("Your cancer risk category is MEDIUM.")
        elif user_input[0] <= 40 and user_input[1] > 2 and user_input[2] >= 5 :
            print("Your cancer risk category is MEDIUM.")
        else:
            print("Your cancer risk category is LOW.")

        if user_input[0] > 40:
            user_input[0] = int(1)
        elif user_input[0] <= 40:
            user_input[0] = int(0)
        if user_input[1] <= 2:
            user_input[1] = int(1)
        elif user_input[1] > 2:
            user_input[1] = int(0)
        if user_input[2] >= 5:
            user_input[2] = int(1)
        elif user_input[2] < 5:
            user_input[2] = int(0)

            
        if user_input == [0,1,1] or user_input == [1,1,0]:
            print("Your cancer risk category will improve if you increase your daily portion of fruit and vegetables.")

        if user_input == [0,0,1] or user_input == [0,1,0]:
            print("Your cancer risk category will worsen after you turn 40 if you don't change your dietary or smoking habits.")

        print("\nThank you for using Cancer Riskbot 3.0. To view the data collected from this conversation, type and enter the follwing: \nhistory")
        if len(history) == 2:      
            for user in user_info:
                answer = input("")
                if answer == "history":
                    print("Data collected from this conversation:\n")
                    for keys,values in history.items():
                        print(keys)
                        print(values)
                return
    

cancer_riskbot_3()

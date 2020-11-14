class user:
    def __init__(self, prompt):
        self.prompt = prompt

    def chatbot():

        print("Hi there! I am Chatbot. To start, please enter your name.")

        name = input("First Name: ")

        print("Nice to meet you,", name, ". What is your year of birth in YYYY format?")

        def YOB():

            global birthYear
            
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

            return

        YOB()
    chatbot()            

questions = ["a) Average portions of fruit and veg per day: \n",
             "b) Years smoking: \n",
]

user_info = [
    user(questions[0]),
    user(questions[1]),
]

age = 2020-birthYear
age_int = int(age)
user_input = [age_int]

print("\n\nIn the next section, you will be talking to Medical Chatbot, who will help you from here.\n\n")

def medical_chatbot():
    print("Hi, I'm Medical Chatbot. I am going to ask you questions about your lifestyle and according to your answers, you will know your risk of cancer.")
    print("\n\nPlease answer the following, by entering data about yourself.\n\n")

    for user in user_info:
        answer = input(user.prompt)
        user_input.append(int(answer))

    if user_input[1] <= 2 and user_input[2] >= 5:
        print("Your cancer risk category is HIGH.")
    elif user_input[2] >= 5 and user_input[0] > 40:
        print("Your cancer risk category is HIGH.")
    elif user_input[1] <= 2 and user_input[2] < 5 and user_input[0] > 40:
        print("Your cancer risk category is MEDIUM.")
    elif user_input[1] > 2 and user_input[2] >= 5 and user_input[0] <= 40:
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
        
    return


medical_chatbot()

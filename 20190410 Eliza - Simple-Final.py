ques = input("Good Day. What is your problem Enter your response here or Q to quit.")
message = ques.lower()
while (message!="q") or (message=="I am feeling great"):
    print("{}".format(message))
    message=input("Enter your response here,  or Q to quit  ")
    print("{}".format(message))



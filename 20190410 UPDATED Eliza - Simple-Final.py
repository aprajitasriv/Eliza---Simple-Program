
question = True
while question:
    str = input('Good day. What is your problem? Enter your response here or Q to quit:')
    print(str)
    if str.lower() == "great" or str.lower() == "q":
        question = False

print('End')


print('Welcome to the Untun101 Quiz Game')
answer=input('Are you ready to play the Quiz ? (y/n) :')
score=0
total_questions=3
 
if answer.lower()=='y':
    answer=input('Question 1: What university do you go to?')
    if answer.lower()=='Sophia' or 'Sophia University' or 'sophia' or 'sophia university':
        score += 1
        print('You got it!よかった')
    else:
        print('Wrong Answer wahwahwahwaaaaaah :(')
 
 
    answer=input('Question 2: What faculty are you in? ')
    if answer.lower()=='FLA' or 'Faculty of Liberal Arts' or 'fla' or 'faculty of liberal arts':
        score += 1
        print('Haha sammmme!')
    else:
        print('I guess we are strangers and NOT strangers at the same time haha')
 
    answer=input('Question 3: Do you have GitHub?')
    if answer.lower()=='Yes' or 'yes' or 'y':
        score += 1
        print('Of course, you do lmaoo')
    else:
        print('I guess you should make one, right? Lmaoo')
 
print('Thank you for playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE! See you in class!')


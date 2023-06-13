# write your code here
Friends={}
import random
Number_of_friends = int(input("Enter the number of friends joining (including you):\n"))
if Number_of_friends <= 0:   
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    x = range(int(Number_of_friends))
    for n in x:
      name=str(input())
      Friends[f"{name}"]=0
    total_bill=float(input('Enter the total bill value:\n'))
    choices= input("Do you want to use the 'Who is lucky?'feature? Write Yes/No:\n")
    divide_bill=round(total_bill/Number_of_friends ,2)
    if choices.lower()=="yes":
        lucky_one=random.choice(list(Friends.keys()))
        print(f"{lucky_one} is the lucky one!")
        Friends[f"{name}"]=0
        Friends_to_pay_bills=Number_of_friends - 1
        Second_divide_bill=round(total_bill/Friends_to_pay_bills,2)
        for d in Friends:
            if d != lucky_one:
                Friends[f"{d}"]= Second_divide_bill
    else:
        print("No one is going to be lucky")
        for d in Friends:
            Friends[f"{d}"]=divide_bill
    print(Friends)

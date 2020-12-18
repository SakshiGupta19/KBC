quesList = ['Capital of India is:', 'How many states are in India:', 'Who is also known as King of BollyWood', 'Who is main Lead of Twilight Film Series' ]
opt1List = ['Bhopal', '35', 'Salman Khan', 'Bella & Edward']
opt2List = ["Delhi", '30', 'Amitabh Bacchan', 'Harry Potter & Hermonie']
opt3List = ['Mumbai', '29', 'Akshay Kumar', 'Jodha & Akbar']
opt4List = ['Bangalore', '27', 'Shah Rukh Khan', 'Veer & Zara']
ansList = [2, 3, 4, 1]
opt5List = [opt2List[0], opt3List[0], opt2List[1], opt3List[1], opt4List[2], opt1List[2], opt3List[3], opt1List[3]]
ans1List = [1,2,1,2]
i = 0
j = 0
k = 1
while i <= 3:
    print(quesList[i])
    print(1, opt1List[i])
    print(2, opt2List[i])
    print(3, opt3List[i])
    print(4, opt4List[i])
    userAns = int(input("Enter the answer") )
    if userAns == ansList[i]:
        print("Congratulations, your answer is correct!")
    
    else:
        print("Your Answer is wrong!")
        print("Do you want to use Lifeline")
        user1Ans = input("Yes or No")
        
        if k >1:
            print("You cannot use lifeline as you used it before")
            break
        
        if user1Ans == "Yes":
            print("Your Options are:")
            print(1, opt5List[j])
            print(2, opt5List[j+1])
            user2Ans = int(input("Enter the Answer"))
            if user2Ans == ans1List[i]:
                print("Congratulations, your answer is correct")
            else:
                print ("Your answer is wrong")
                break
        elif user1Ans == "No":
            break
        else:
            print("You entered wrong input please try again")
            break
        k = k +1
    i = i +1
    j = j +2
print("Thanks for Playing")
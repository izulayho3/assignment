bottle=input("Enter the number of bottles:")
student=input("Are you a student? (yes/no):")
money=input("Enter the money you have:")
bottle=int(bottle)
money=int(money)
if student =='yes':
    if bottle >= 8 :
        print(Price per bottle: 2)
        money_1=bottle*2
    else:
        print(Price per bottle: 2)
        money_2=bottle*4
else:
    if bottle >= 8 :
        print(Price per bottle: 4)
        money_3=bottle*4
    else:
     print(Price per bottle: 6)
    money_4=bottle*6
if money_1<money:
    print("Total cost: ",money_1) 
    print("Money left: ",money- money_1)
elif money_2<money:
    print("Total cost: ",money_2)   
    print("Money left: ",money - money_2)
elif money_3<money:
    print("Total cost: ",money_3)   
    print("Money left: ",money - money_3)
elif money_4<money:
    print("Total cost: ",money_4)   
    print("Money left: ",money - money_4)
if (money_1>money): 
    print("Total cost: ",money_1) 
    print("Money left: ",money - money_1)
elif money_2>money:
    print("Total cost: ",money_2)   
    print("Money left: ",money - money_2)
elif money_3>money:
    print("Total cost: ",money_3)   
    print("Money left: ",money - money_3)
elif money_4>money:
    print("Total cost: ",money_4)   
    print("Money left: ",money - money_4)
if (money_1>money) :
     print("Total cost: ",money_1 )
     print("Money left: ",money - money_1)
elif money_2>money:
    print("Total cost: ",money_2)   
    print("Money left: ",money - money_2)
elif money_3>money:
    print("Total cost: ",money_3)   
    print("Money left: ",money - money_3)
elif money_4>money:
    print("Total cost: ",money_4)   
    print("Money left: ",money - money_4)
if money == money_1:
    print('Total cost:',money_1)
    print ('Exactly enough money')
elif money == money_2:
    print ('Total cost:',money_2)
    print('Exactly enough money')
elif money == money_3:
    print ('Total cost:',money_3)
    print('Exactly enough money')
elif money == money_4:
    print('Total cost:',money_4)
    print('Exactly enough money')
    

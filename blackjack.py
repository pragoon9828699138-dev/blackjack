
from random import randint

print("-----------")
print("YOUR TURN")
print("-----------")
a=randint(1,13)
b=randint(1,13)
if a==1:
    print("Drew an Ace")
    a_value=11
elif a==11:
    print("Drew a Jack")
    a_value=10
elif a==12:
    print("Drew a Queen")
    a_value=10
elif a==13:
    print("Drew a King")
    a_value=10
elif a==8:
    print("Drew an "+ str(a))
    a_value=a
else:
    print("Drew a "+str(a))
    a_value=a
if b==1:
    print("Drew an Ace")
    b_value=11
elif b==11:
    print("Drew a Jack")
    b_value=10
elif b==12:
    print("Drew a Queen")
    b_value=10
elif b==13:
    print("Drew a King")
    b_value=10
elif b==8:
    print("Drew an "+ str(b))
    b_value=b
else:
    print("Drew a "+str(b))
    b_value=b
hand_value=a_value+b_value
while hand_value<21:
 c=input(f"You have {hand_value}. Hit (y/n)? ")
 if c=="y":
     d=randint(1,13)
     if d==1: 
         print("Drew an Ace")
         d_value=11
     elif d==11:
         print("Drew a Jack")
         d_value=10
     elif d==12:
         print("Drew a Queen")
         d_value=10
     elif d==13:
         print("Drew a King")
         d_value=10
     elif d==8:
         print("Drew an "+ str(d))
         d_value=d
     else:
         print("Drew a "+str(d))
         d_value=d
     hand_value+=d_value
 elif c=="n":
     break
 else:
     print("Sorry I didn't get that.")
print(f"Final hand: {hand_value}.")
if hand_value==21:
    print("BLACKJACK!")
elif hand_value>21:
    print("BUST.")
print("-----------")
print("DEALER TURN")
print("-----------")
x=randint(1,13)
y=randint(1,13)
if x==1:
    print("Drew an Ace")
    x_value=11
elif x==11:
    print("Drew a Jack")
    x_value=10
elif x==12:
    print("Drew a Queen")
    x_value=10
elif x==13:
    print("Drew a King")
    x_value=10
elif x==8:
    print("Drew an "+ str(x))
    x_value=x
else:
    print("Drew a "+str(x))
    x_value=x
if y==1:
    print("Drew an Ace")
    y_value=11
elif y==11:
    print("Drew a Jack")
    y_value=10
elif y==12:
    print("Drew a Queen")
    y_value=10
elif y==13:
    print("Drew a King")
    y_value=10
elif y==8:
    print("Drew an "+ str(y))
    y_value=y
else:
    print("Drew a "+str(y))
    y_value=y
hand_value1=x_value+y_value
if hand_value1<17:
    print(f"Dealer has {hand_value1}.")
while hand_value1<17:
    h=randint(1,13)
    if h==1:
        print("Drew an Ace")
        h_value=11
    elif h==11:
        print("Drew a Jack")
        h_value=10
    elif h==12:
        print("Drew a Queen")
        h_value=10
    elif h==13:
        print("Drew a King")
        h_value=10
    elif h==8:
        print("Drew an "+ str(h))
        h_value=h
    else:
        print("Drew a "+str(h))
        h_value=h
    hand_value1+=h_value
    if hand_value1<17:
        print(f"Dealer has {hand_value1}.")
print(f"Final hand: {hand_value1}.")
if hand_value1==21:
    print("BLACKJACK!")
elif hand_value1>21:
    print("BUST.")
print("-----------")
print("GAME RESULT")
print("-----------")
RED="\033[91m"
GREEN="\033[92m"
RESET="\033[0m"
if hand_value>21:
    print(RED+"Dealer wins!")
elif hand_value1>21:
    print(GREEN+"You win!"+RESET)
elif hand_value>hand_value1:
    print(GREEN+"You win!"+RESET)
elif hand_value1>hand_value:
    print(RED+"Dealer wins!"+RESET)
else:
    print("Push.")



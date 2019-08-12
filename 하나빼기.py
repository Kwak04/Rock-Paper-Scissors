# 하나빼기.py

import random
import time

print("하나빼기?")
print()

user1 = input("두 개 중 하나는 무엇을 내시겠어요? (가위/바위/보) : ")

while user1 != "가위" and user1 != "바위" and user1 != "보":
    user1 = input("두 개 중 하나는 무엇을 내시겠어요? (**가위/바위/보**) : ")

user2 = input("나머지 하나는요? (두 개가 달라야 합니다.) (가위/바위/보) : ")

while user2 != "가위" and user2 != "바위" and user2 != "보":
    user2 = input("나머지 하나는요? (**두 개가 달라야 합니다.**) (**가위/바위/보**) : ")

while user1 == user2:
    user2 = input("나머지 하나는요? (두 개가 달라야 합니다.) (가위/바위/보) : ")
    
com1 = random.choice(["가위", "바위", "보"])
com2 = random.choice(["가위", "바위", "보"])
while com1 == com2:
    com1 = random.choice(["가위", "바위", "보"])
    com2 = random.choice(["가위", "바위", "보"])
print()

print("가위")
time.sleep(0.5)
print("바위")
time.sleep(0.5)
print("보!")
time.sleep(0.5)
print()

print("컴퓨터 :  %s   %s" % (com1, com2))
print(" 당신  :  %s   %s" % (user1, user2))

print()
user = input("%s와 %s 중 무엇을 내시겠어요? : " % (user1, user2))
while user != user1 and user != user2:
    user = input("%s와 %s 중 무엇을 내시겠어요? : " % (user1, user2))
com = random.choice([com1, com2])
print()

print("하나")
time.sleep(0.5)
print("빼")
time.sleep(0.5)
print("기!")
time.sleep(0.5)
print()

print("당신은 %s를 냈고 컴퓨터는 %s를 냈습니다!" % (user, com))

if (user == "가위" and com == "보") or (user == "바위" and com == "가위") or (user == "보" and com == "바위"):
    print("이겼어요!!")
elif (user == "가위" and com == "바위") or (user == "바위" and com == "보") or (user == "보" and com == "가위"):
    print("졌네요..")
elif user == com:
    print("비겼네요!")
else:
    print("이상한거 내지 말라구욧!")

print()
input("엔터키를 눌러 종료하세요 . . . ")

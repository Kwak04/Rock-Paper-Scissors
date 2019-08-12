# 가위바위보.py

import random
import time

print("★가위바위보★")
user, com = 0, 0

while user == com:
    print()
    user = input("무엇을 내실 건가요? (가위/바위/보) : ")
    com = random.choice(["가위", "바위", "보"])

    print()
    print("가위")
    time.sleep(0.5)
    print("바위")
    time.sleep(0.5)
    print("보!")
    time.sleep(0.5)
    print()
    print("컴퓨터 : %s" % com)
    print(" 당신  : %s" % user)

    if (user == "가위" and com == "보") or (user == "바위" and com == "가위") or (user == "보" and com == "바위"):
        print("이겼네요!")
    if (user == "가위" and com == "바위") or (user == "바위" and com == "보") or (user == "보" and com == "가위"):
        print("졌네요..")
    if user == com:
        print("비겼네요. 다시 해 주세요!")

    else:
        print("이상한거 내지 말라구욧!")

# 묵찌빠.py

import random
import time

print("묵찌빠!")

attack = " "
user_ = " "
count = 0


def whattosay(cnt, old, new):
    if cnt == 0:
        print("가위")
        time.sleep(0.5)
        print("바위")
        time.sleep(0.5)
        print("보!")
        time.sleep(0.5)
    else:
        print(old)
        time.sleep(0.5)
        print(old)
        time.sleep(0.5)
        print("%s!" % new)


while True:
    print()
    user = input("무엇을 내실 건가요? (묵/찌/빠) : ")
    while user != "묵" and user != "찌" and user != "빠":
        user = input("무엇을 내실 건가요? (**묵/찌/빠**) :")
    com = random.choice(["묵", "찌", "빠"])
    print()
    whattosay(count, user_, user)
    user_ = user

    print()
    print("컴퓨터 : %s" % com)
    print(" 당신  : %s" % user)


    # 같은 것을 냈을 때
    if user == com:
        if attack == "user":  # 공격권이 사용자에게 있을 때
            print("이겼네요!")
            break
        elif attack == "com":  # 공격권이 컴퓨터에게 있을 때
            print("졌네요..")
            break
        else:  # 공격권이 아무에게도 없을 때
            print("비겼습니다. 다시 해 주세요.")

    # 다른 것을 냈을 때
    else:
        count += 1  # 가위 바위 보! ==> 묵찌빠

        # 사용자가 이겼을 때
        if (user == "묵" and com == "찌") or (user == "찌" and com == "빠") or (user == "빠" and com == "묵"):
            print("당신이 이겼으므로 공격권을 가지게 되었습니다!")
            attack = "user"
        # 컴퓨터가 이겼을 때
        else:
            print("컴퓨터가 이겼으므로 공격권을 뺏겼습니다!")
            attack = "com"

# 게임 종료
print("\n끝!")

# 3종세트.py
# 가위바위보 + 하나빼기 + 묵찌빠

import random
import time


# 가위바위보
def type_1():
    print("■ 가위바위보")
    print("==============================================================")

    user, com = 0, 0

    while user == com:
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
        elif (user == "가위" and com == "바위") or (user == "바위" and com == "보") or (user == "보" and com == "가위"):
            print("졌네요..")
        elif user == com:
            print("비겼네요. 다시 해 주세요!")
        else:
            print("이상한거 내지 말라구욧!")


# 하나빼기
def type_2():
    print("■ 하나빼기")
    print("==============================================================")
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

    print("컴퓨터 : %s" % com)
    print(" 당신  : %s" % user)

    if (user == "가위" and com == "보") or (user == "바위" and com == "가위") or (user == "보" and com == "바위"):
        print("이겼어요!!")
    elif (user == "가위" and com == "바위") or (user == "바위" and com == "보") or (user == "보" and com == "가위"):
        print("졌네요..")
    elif user == com:
        print("비겼네요!")
    else:
        print("이상한거 내지 말라구욧!")


# 묵찌빠
def type_3():
    print("■ 묵찌빠")
    print("==============================================================")

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


print("1. 가위바위보\n2. 하나빼기\n3. 묵찌빠")
what = 0

while True:
    what = int(input("숫자로 입력하세요 : "))
    if what == 1:
        type_1()
        break
    elif what == 2:
        type_2()
        break
    elif what == 3:
        type_3()
        break
    else:
        print("다시 입력하세요!")

print()
print("프로그램이 끝났습니다.")
input("엔터키를 눌러 종료하세요 . . .")

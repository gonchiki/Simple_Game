import numpy as np

x = ["グー","チョキ","パー"]

#コンピュータのコメント
c_lose = "ま、負けたぁ"
c_win = "フハハハハハハハハ！！！！"


def janken():
    print("じゃーんけん、ぽんっ！！")
    u = input("出す手を次の３つからきめてね：（グー：0,チョキ：1,パー：2）")
    i = int(u)
    your = x[i]
    computer = np.random.choice(x)

    if your == computer:
        print("iQos　あ、あいこっす")
    elif (your == x[0]) and (computer == x[1]):
        print(c_lose)
    elif (your == x[1]) and (computer == x[2]):
        print(c_lose)
    elif (your == x[2]) and (computer == x[0]):
        print(c_lose)
    else:
        print(c_win)

janken()

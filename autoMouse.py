from pykeyboard import PyKeyboard
import random
import time
import sys

k = PyKeyboard()
mode = ['E','X','3','4','5','A','D','W','S']

# 随机按键
def randomClick():
    while True:
        try:
            interval = random.randint(0,20)
            time.sleep(interval)
            r = random.randint(0, len(mode))
            key = mode[r]
            print(key)
            k.tap_key(key)

        except Exception as e:
            print (e)

if __name__=="__main__":
    randomClick()
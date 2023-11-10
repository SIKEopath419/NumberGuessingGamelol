import random

def guess_the_number():
    # 步驟 1: 隨機生成目標數字
    target_number = random.randint(x1, x2)
    
    # 步驟 2: 玩家猜測數字的主迴圈
    attempts = 0
    max_attempts = n
    
    while attempts < max_attempts:
        # 玩家輸入猜測的數字
        guess = int(input("猜一個數字（{x1}-{x2}）："))
        
        # 步驟 3: 提供反饋
        if guess == target_number:
            print("矮唷猜對了，看來你智商還算正常")
            break
        elif guess < target_number:
            print("太小")
        else:
            print("太大")
        
        attempts += 1
    
    # 步驟 4: 結束遊戲
    if attempts == max_attempts:
        print(f"你猜了 {max_attempts} 次還是沒中你也很天才。答案是 {target_number}。")

if __name__ == "__main__":
    guess_the_number()

#==========================================================================================================================================

import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import messagebox
import random

# 讀取XML配置文件
tree = ET.parse('config.xml')
root = tree.getroot()

x1 = int(root.find('x1').text)
x2 = int(root.find('x2').text)
n = int(root.find('n').text)
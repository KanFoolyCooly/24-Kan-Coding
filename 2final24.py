"""

เลือกโจทย์: โปรแกรมทายตัวเลข 1-10
I : รับอินพุตจากผู้ใช 1-10 คือ guess
P : โค้ดสุ่มเลข 1-10 คือ digit และ เช็กคำตองผู้ใช้ คือ process
O : ถ้า guess ตรงกับ digit process = ถูก ถ้าไม่ = ผิด
ตัวแปร: guess, digit, proess

"""
# โปรแกรมทายเลข 1-10

import random

digit = random.randint(1, 10)

input("สวัสดีครับมาลองโปรแกรมกัน(กดปุ่มenterเพื่อเริ่ม)")

while True:

    guess = int(input("ทายเลขมาเลย (1-10): "))

    if guess == digit:
        print("ถ ถ ถูก✔")
        print("\nเครดิต นายกันตวิชญ์ ซอพรมราช ✔")
        break
    else:
        print("❌ ผิด ลองใหม่ดูนะ")
        print('\n')

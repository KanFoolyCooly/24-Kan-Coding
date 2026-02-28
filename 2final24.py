"""

เลือกโจทย์: โปรแกรมทายตัวเลข 1-10
I : รับอินพุตจากผู้ใช 1-10 คือ guess
P : โค้ดสุ่มเลข 1-10 คือ digit และ เช็กคำตองผู้ใช้ คือ process
O : ถ้า guess ตรงกับ digit process = ถูก ถ้าไม่ = ผิด
ตัวแปร: guess, digit, proess

"""

"""
# โปรแกรมทายเลข 1-10 เขียนเอง

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
"""
"""
#Ai เพิ่มเติม Gui 
import tkinter as tk
import random

# สุ่มเลข
digit = random.randint(1, 10)

# ฟังก์ชันเช็คคำตอบ
def check_guess():
    global digit
    try:
        guess = int(entry.get())
        if guess == digit:
            result_label.config(
                text="🎉 ถูกต้อง!!! 🎉",
                fg="#00ff88"
            )
            credit_label.config(
                text="เครดิต นายกันตวิชญ์ ซอพรมราช ✔",
                fg="white"
            )
            digit = random.randint(1, 10)  # สุ่มใหม่หลังทายถูก
        else:
            result_label.config(
                text="❌ ผิด ลองใหม่!",
                fg="#ff4444"
            )
    except ValueError:
        result_label.config(
            text="⚠ กรุณาใส่ตัวเลขเท่านั้น",
            fg="yellow"
        )

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("🎮 เกมทายเลข 1-10")
root.geometry("400x300")
root.configure(bg="#1e1e2f")

# หัวข้อเกม
title_label = tk.Label(
    root,
    text="🎯 เกมทายเลข 1-10 🎯",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="#00ffff"
)
title_label.pack(pady=15)

# ช่องกรอกตัวเลข
entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center"
)
entry.pack(pady=10)

# ปุ่มทาย
guess_button = tk.Button(
    root,
    text="🔥 ทายเลย!",
    font=("Arial", 14, "bold"),
    bg="#ff8800",
    fg="white",
    activebackground="#ffaa33",
    command=check_guess
)
guess_button.pack(pady=10)

# แสดงผลลัพธ์
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="#1e1e2f"
)
result_label.pack(pady=10)

# เครดิต
credit_label = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    bg="#1e1e2f"
)
credit_label.pack(pady=5)

root.mainloop()

"""

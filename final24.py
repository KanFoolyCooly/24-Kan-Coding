"""

เลือกโจทย์: โปรแกรมทายตัวเลข 1-10
I : รับอินพุตจากผู้ใช 1-10 คือ guess
P : โค้ดสุ่มเลข 1-10 คือ digit และ เช็กคำตองผู้ใช้ คือ process
O : ถ้า guess ตรงกับ digit process = ถูก ถ้าไม่ = ผิด
ตัวแปร: guess, digit, proess

"""

# โปรแกรมทายเลข 1-10 แบบ GUI ว-1.11

import tkinter as tk
import random

# สุ่มเลข
digit = random.randint(1, 10)

# ฟังก์ชันตรวจคำตอบ
def check_guess():
    try:
        guess = int(entry.get())
        if guess == digit:
            result_label.config(text="✔ ถูกแล้ว โชคดีไปนะ 😒👌",
                                fg="green")
            credit_label.config(text="เครดิต นายกันตวิชญ์ ซอพรมราช ✔")
            button.config(state="disabled")  # ปิดปุ่มเมื่อชนะ
        else:
            result_label.config(text="❌ ยังผิด ลองใหม่อีกครั้ง",
                                fg="red")
            entry.delete(0, tk.END)
    except:
        result_label.config(text="กรุณาใส่ตัวเลข 1-10 เท่านั้น!",
                            fg="orange")

# สร้างหน้าต่าง
window = tk.Tk()
window.title("เกมทายเลข 1-10 🎯")
window.geometry("400x300")
window.resizable(False, False)

# ข้อความอธิบาย
title_label = tk.Label(window, text="ถ้านายทายถูก นายชนะ 🎉\nถ้าผิดก็ลองใหม่ 😂",
                       font=("Arial", 14))
title_label.pack(pady=15)

# ช่องกรอกเลข
entry = tk.Entry(window, font=("Arial", 16), justify="center")
entry.pack(pady=10)

# ปุ่มตรวจคำตอบ
button = tk.Button(window, text="ทายเลย!", font=("Arial", 12),
                   command=check_guess)
button.pack(pady=10)

# แสดงผลลัพธ์
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=5)

# เครดิต
credit_label = tk.Label(window, text="", font=("Arial", 10))
credit_label.pack(pady=10)

window.mainloop()

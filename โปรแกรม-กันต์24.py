import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        unit = float(entry_unit.get())
        price_per_unit = 4

        electric_cost = unit * price_per_unit
        service_fee = (electric_cost // 500) * 50
        if electric_cost % 500 != 0:
            service_fee += 50

        total_cost = electric_cost + service_fee

        label_electric.config(
            text=f"⚡ ค่าไฟฟ้า: {electric_cost:,.2f} บาท"
        )
        label_service.config(
            text=f"🧾 ค่าบริการ: {service_fee:,.2f} บาท"
        )
        label_total.config(
            text=f"{total_cost:,.2f} บาท"
        )

    except ValueError:
        messagebox.showerror("ข้อผิดพลาด ❌", "กรุณากรอกจำนวนหน่วยเป็นตัวเลข")

def on_enter(e):
    btn_calculate["bg"] = "#163a5f"

def on_leave(e):
    btn_calculate["bg"] = "#1f4e79"

# ===== หน้าต่างหลัก =====
root = tk.Tk()
root.title("🏛️ ระบบคำนวณค่าไฟฟ้า")

# ขนาดพอดีกับทุกองค์ประกอบ
root.geometry("880x560")

# ล็อคขนาดหน้าต่าง
root.resizable(False, False)

root.configure(bg="#e9eef3")

# ===== Header =====
header = tk.Frame(root, bg="#1f4e79", height=80)
header.pack(fill="x")

tk.Label(
    header,
    text="🏛️ ระบบคำนวณค่าไฟฟ้า | Electricity Cost Calculator",
    bg="#1f4e79",
    fg="white",
    font=("Tahoma", 20, "bold")
).pack(padx=24, pady=22, anchor="w")

# ===== Content =====
content = tk.Frame(root, bg="white", bd=1, relief="solid")
content.pack(padx=40, pady=25, fill="both", expand=True)

tk.Label(
    content,
    text="📊 กรอกข้อมูลการใช้ไฟฟ้า",
    bg="white",
    font=("Tahoma", 16, "bold"),
    fg="#1f4e79"
).pack(pady=(25, 10))

tk.Label(
    content,
    text="🔢 จำนวนหน่วยไฟฟ้าที่ใช้ (หน่วย):",
    bg="white",
    font=("Tahoma", 12)
).pack(pady=6)

entry_unit = tk.Entry(
    content,
    font=("Tahoma", 14),
    justify="center",
    width=20
)
entry_unit.pack(pady=8)

btn_calculate = tk.Button(
    content,
    text="⚡ คำนวณค่าไฟฟ้า",
    font=("Tahoma", 13, "bold"),
    bg="#1f4e79",
    fg="white",
    width=22,
    relief="flat",
    command=calculate
)
btn_calculate.pack(pady=14)
btn_calculate.bind("<Enter>", on_enter)
btn_calculate.bind("<Leave>", on_leave)

# ===== Result Section =====
result_frame = tk.Frame(content, bg="#f8fbff")
result_frame.pack(pady=10, padx=40, fill="x")

label_electric = tk.Label(
    result_frame,
    text="⚡ ค่าไฟฟ้า: -",
    bg="#f8fbff",
    font=("Tahoma", 12),
    anchor="w"
)
label_electric.pack(anchor="w", pady=4)

label_service = tk.Label(
    result_frame,
    text="🧾 ค่าบริการ: -",
    bg="#f8fbff",
    font=("Tahoma", 12),
    anchor="w"
)
label_service.pack(anchor="w", pady=4)

# ===== Highlight Total =====
total_frame = tk.Frame(
    result_frame,
    bg="white",
    bd=3,
    relief="solid"
)
total_frame.pack(pady=12, fill="x")

tk.Label(
    total_frame,
    text="💰 รวมเป็นเงินทั้งสิ้น",
    bg="white",
    font=("Tahoma", 13, "bold"),
    fg="#1f4e79"
).pack(pady=(10, 2))

label_total = tk.Label(
    total_frame,
    text="- บาท",
    bg="white",
    font=("Tahoma", 18, "bold"),
    fg="#163a5f"
)
label_total.pack(pady=(0, 12))

# ===== Footer =====
tk.Label(
    root,
    text="ℹ️ ตัวอย่างระบบเพื่อการศึกษา | รูปแบบเว็บไซต์ราชการ",
    bg="#e9eef3",
    font=("Tahoma", 10),
    fg="gray"
).pack(pady=6)

root.mainloop()

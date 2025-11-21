import math
import tkinter as tk
from tkinter import messagebox



def haversine_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    R = 6378137  # شعاع زمین به متر
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_perimeter(p1, p2, p3):
    """محاسبه محیط مثلث"""
    lat1, lon1 = p1
    lat2, lon2 = p2
    lat3, lon3 = p3
    d12 = haversine_distance(lat1, lon1, lat2, lon2)
    d23 = haversine_distance(lat2, lon2, lat3, lon3)
    d31 = haversine_distance(lat3, lon3, lat1, lon1)
    
    if d12 == 0 or d23 == 0 or d31 == 0:
        return None

    if not is_valid_triangle(d12, d23, d31):
        return None

    return d12 + d23 + d31

def triangle_area(p1, p2, p3):
    """محاسبه مساحت مثلث با فرمول هرون"""
    lat1, lon1 = p1
    lat2, lon2 = p2
    lat3, lon3 = p3
    a = haversine_distance(lat1, lon1, lat2, lon2)
    b = haversine_distance(lat2, lon2, lat3, lon3)
    c = haversine_distance(lat3, lon3, lat1, lon1)

    if not is_valid_triangle(a, b, c):
        return None

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# ---------- تابع دکمه محاسبه ----------

def calculate():
    try:
        lat1 = float(entry_lat1.get())
        lon1 = float(entry_lon1.get())
        lat2 = float(entry_lat2.get())
        lon2 = float(entry_lon2.get())
        lat3 = float(entry_lat3.get())
        lon3 = float(entry_lon3.get())

        p1, p2, p3 = (lat1, lon1), (lat2, lon2), (lat3, lon3)
        perimeter = triangle_perimeter(p1, p2, p3)
        area = triangle_area(p1, p2, p3)

        if perimeter is None or area is None:
            messagebox.showerror("خطا", "مثلث معتبر نیست یا نقاط یکسان هستند!")
        else:
            messagebox.showinfo(
                "نتیجه",
                f"محیط مثلث: {perimeter:.2f} متر\nمساحت مثلث: {area:.2f} متر مربع"
            )
    except ValueError:
        messagebox.showerror("خطا", "لطفاً همه مقادیر را به درستی وارد کنید!")

# ---------- رابط کاربری ----------

root = tk.Tk()
root.title("محیط و مساحت مثلث بر اساس مختصات جغرافیایی")

# نقطه 1
tk.Label(root, text="نقطه 1").grid(row=0, column=0, columnspan=2)
tk.Label(root, text="Lat1:").grid(row=1, column=0)
tk.Label(root, text="Lon1:").grid(row=2, column=0)
entry_lat1 = tk.Entry(root)
entry_lon1 = tk.Entry(root)
entry_lat1.grid(row=1, column=1)
entry_lon1.grid(row=2, column=1)

# نقطه 2
tk.Label(root, text="نقطه 2").grid(row=3, column=0, columnspan=2)
tk.Label(root, text="Lat2:").grid(row=4, column=0)
tk.Label(root, text="Lon2:").grid(row=5, column=0)
entry_lat2 = tk.Entry(root)
entry_lon2 = tk.Entry(root)
entry_lat2.grid(row=4, column=1)
entry_lon2.grid(row=5, column=1)

# نقطه 3
tk.Label(root, text="نقطه 3").grid(row=6, column=0, columnspan=2)
tk.Label(root, text="Lat3:").grid(row=7, column=0)
tk.Label(root, text="Lon3:").grid(row=8, column=0)
entry_lat3 = tk.Entry(root)
entry_lon3 = tk.Entry(root)
entry_lat3.grid(row=7, column=1)
entry_lon3.grid(row=8, column=1)

# دکمه محاسبه
btn_calc = tk.Button(root, text="محاسبه محیط و مساحت", command=calculate)
btn_calc.grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()

# import math
# def haversine_distance(lat1, lon1, lat2, lon2):
#     lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
#     R = 6378137
#     dlat = lat2 - lat1
#     dlon = lon2 - lon1
#     a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#     return R * c  
# def is_valid_triangle(a, b, c):
#     return a + b > c and a + c > b and b + c > a
# def triangle_perimeter(p1, p2, p3):
#     lat1, lon1 = p1
#     lat2, lon2 = p2
#     lat3, lon3 = p3
#     d12 = haversine_distance(lat1, lon1, lat2, lon2)
#     d23 = haversine_distance(lat2, lon2, lat3, lon3)
#     d31 = haversine_distance(lat3, lon3, lat1, lon1)
#     if d12 == 0 or d23 == 0 or d31 == 0:
#         return "error"

#     if not is_valid_triangle(d12, d23, d31):
#         return "error"

#     return d12 + d23 + d31

# p1 = input("enter (lat1, lon1):") 
# p2 = input("enter (lat2, lon2):")
# p3 = input("enter (lat3, lon3):")

# perimeter = triangle_perimeter(p1, p2, p3)
# print("perimeter:", perimeter)

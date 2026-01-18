import tkinter as tk
from tkinter import filedialog, messagebox
from caesar_cipher.caesar import caesar, vigenere

# ================== Functions ==================

def process():
    text = text_box.get("1.0", tk.END).strip().lower()
    direction = mode.get()

    if cipher_type.get() == "caesar":
        try:
            shift = int(shift_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Shift must be a valid number")
            return
        result = caesar(text, shift, direction)
    else:
        key = key_entry.get().strip()
        if not key.isalpha():
            messagebox.showerror("Error", "Vigenère key must contain letters only")
            return
        result = vigenere(text, key, direction)

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result)


def reset():
    text_box.delete("1.0", tk.END)
    result_box.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)


def save_text():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(result_box.get("1.0", tk.END))


def load_text():
    file = filedialog.askopenfilename()
    if file:
        with open(file, "r", encoding="utf-8") as f:
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, f.read())


def copy_result():
    root.clipboard_clear()
    root.clipboard_append(result_box.get("1.0", tk.END))
    messagebox.showinfo("Copied", "Result copied to clipboard")

# ================== Window ==================

root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("650x500")
root.resizable(False, False)

# ================== Title ==================

top_frame = tk.Frame(root, pady=10)
top_frame.pack()

tk.Label(
    top_frame,
    text="🔐 Encryption Tool",
    font=("Arial", 16, "bold")
).pack()

# ================== Input ==================

input_frame = tk.LabelFrame(root, text="Input Text", padx=10, pady=10)
input_frame.pack(fill="x", padx=15)

text_box = tk.Text(input_frame, height=4)
text_box.pack(fill="x")

# ================== Options ==================

options_frame = tk.LabelFrame(root, text="Settings", padx=10, pady=10)
options_frame.pack(fill="x", padx=15, pady=5)

# Mode
mode = tk.StringVar(value="encode")
tk.Radiobutton(options_frame, text="Encode", variable=mode, value="encode").grid(row=0, column=0)
tk.Radiobutton(options_frame, text="Decode", variable=mode, value="decode").grid(row=0, column=1)

# Cipher type
cipher_type = tk.StringVar(value="caesar")
tk.Radiobutton(options_frame, text="Caesar", variable=cipher_type, value="caesar").grid(row=0, column=2)
tk.Radiobutton(options_frame, text="Vigenère", variable=cipher_type, value="vigenere").grid(row=0, column=3)

# Shift
tk.Label(options_frame, text="Shift:").grid(row=1, column=0, pady=5)
shift_entry = tk.Entry(options_frame, width=10)
shift_entry.grid(row=1, column=1)

# Key
tk.Label(options_frame, text="Key (Vigenère):").grid(row=1, column=2)
key_entry = tk.Entry(options_frame, width=10)
key_entry.grid(row=1, column=3)

# ================== Buttons ==================

buttons_frame = tk.Frame(root, pady=10)
buttons_frame.pack()

tk.Button(buttons_frame, text="Run", width=12, command=process).grid(row=0, column=0, padx=5)
tk.Button(buttons_frame, text="Reset", width=12, command=reset).grid(row=0, column=1, padx=5)
tk.Button(buttons_frame, text="Load", width=12, command=load_text).grid(row=0, column=2, padx=5)
tk.Button(buttons_frame, text="Save", width=12, command=save_text).grid(row=0, column=3, padx=5)
tk.Button(buttons_frame, text="Copy", width=12, command=copy_result).grid(row=0, column=4, padx=5)

# ================== Result ==================

result_frame = tk.LabelFrame(root, text="Result", padx=10, pady=10)
result_frame.pack(fill="x", padx=15)

result_box = tk.Text(result_frame, height=4)
result_box.pack(fill="x")

# ================== Footer ==================

footer = tk.Frame(root)
footer.pack(side="bottom", fill="x", pady=5)

tk.Label(
    footer,
    text="Developed by Amer Riyad",
    font=("Arial", 9),
    fg="gray"
).pack(side="left", padx=10)

# Optional image (top-right / footer)
try:
    photo = tk.PhotoImage(file="profile.png")
    photo = photo.subsample(6, 6)
    tk.Label(footer, image=photo).pack(side="right", padx=10)
except:
    pass

root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from caesar_cipher import caesar, vigenere

def process():
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Shift must be a number")
        return

    text = text_box.get("1.0", tk.END).strip().lower()
    result = caesar(text, shift, mode.get())
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result)

def reset():
    text_box.delete("1.0", tk.END)
    result_box.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)
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

# ===== Window =====
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("500x400")

# ===== Input Text =====
tk.Label(root, text="Input Text").grid(row=0, column=0, sticky="w")
text_box = tk.Text(root, height=5, width=50)
text_box.grid(row=1, column=0, columnspan=4, pady=5)

# ===== Shift =====
tk.Label(root, text="Shift").grid(row=2, column=0, sticky="w")
shift_entry = tk.Entry(root, width=10)
shift_entry.grid(row=2, column=1, sticky="w")

# ===== Mode =====
mode = tk.StringVar(value="encode")
tk.Radiobutton(root, text="Encode", variable=mode, value="encode").grid(row=2, column=2)
tk.Radiobutton(root, text="Decode", variable=mode, value="decode").grid(row=2, column=3)

# ===== Buttons =====
tk.Button(root, text="Run", command=process).grid(row=3, column=0, pady=10)
tk.Button(root, text="Reset", command=reset).grid(row=3, column=1)

# ===== Result =====
tk.Label(root, text="Result").grid(row=4, column=0, sticky="w")
result_box = tk.Text(root, height=5, width=50)
result_box.grid(row=5, column=0, columnspan=4, pady=5)
tk.Button(root, text="Load", command=load_text).grid(row=3, column=2)
tk.Button(root, text="Save", command=save_text).grid(row=3, column=3)
tk.Button(root, text="Copy", command=copy_result).grid(row=6, column=0)

root.mainloop()

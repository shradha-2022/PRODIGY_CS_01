import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            if char.islower():
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            result += char
    return result

def encrypt(text, shift):
    return caesar_cipher(text, shift, mode='encrypt')

def decrypt(text, shift):
    return caesar_cipher(text, shift, mode='decrypt')

def on_encrypt():
    text = entry_text.get()
    shift = entry_shift.get()
    if not text:
        messagebox.showerror("Invalid Input", "Text cannot be empty.")
        return
    try:
        shift = int(shift)
        encrypted_text = encrypt(text, shift)
        result_var.set(encrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift must be an integer.")

def on_decrypt():
    text = entry_text.get()
    shift = entry_shift.get()
    if not text:
        messagebox.showerror("Invalid Input", "Text cannot be empty.")
        return
    try:
        shift = int(shift)
        decrypted_text = decrypt(text, shift)
        result_var.set(decrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift must be an integer.")

app = tk.Tk()
app.title("Caesar Cipher")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Text:").grid(row=0, column=0, sticky="w")
entry_text = tk.Entry(frame, width=50)
entry_text.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Shift:").grid(row=1, column=0, sticky="w")
entry_shift = tk.Entry(frame, width=10)
entry_shift.grid(row=1, column=1, padx=5, pady=5, sticky="w")

result_var = tk.StringVar()
tk.Label(frame, text="Result:").grid(row=2, column=0, sticky="w")
tk.Entry(frame, textvariable=result_var, width=50, state="readonly").grid(row=2, column=1, padx=5, pady=5)

tk.Button(frame, text="Encrypt", command=on_encrypt).grid(row=3, column=0, pady=5)
tk.Button(frame, text="Decrypt", command=on_decrypt).grid(row=3, column=1, pady=5, sticky="w")

app.mainloop()

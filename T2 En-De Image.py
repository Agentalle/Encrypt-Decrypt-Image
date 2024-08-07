from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("800x310")

def xor_process(file_name, key):
    with open(file_name, 'rb') as file:
        image = bytearray(file.read())
        
    for index, value in enumerate(image):
        image[index] = value ^ int(key)
    
    with open(file_name, 'wb') as file:
        file.write(image)

def encrypt_image():
    file_name = filedialog.askopenfilename(filetypes=[('jpg file', '*.jpg')])
    if file_name:
        key = entry_key.get().strip()
        xor_process(file_name, key)
        print(f"Image encrypted with key: {key}")

def decrypt_image():
    file_name = filedialog.askopenfilename(filetypes=[('jpg file', '*.jpg')])
    if file_name:
        key = entry_key.get().strip()
        xor_process(file_name, key)
        print(f"Image decrypted with key: {key}")

b_encrypt = Button(root, text="Encrypt Image", command=encrypt_image)
b_encrypt.place(x=300, y=100)

b_decrypt = Button(root, text="Decrypt Image", command=decrypt_image)
b_decrypt.place(x=300, y=150)

entry_key = Entry(root, width=10)
entry_key.place(x=320, y=200)

root.mainloop()

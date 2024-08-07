# Encrypt-Decrypt-Image
**Aim**:
This project provides a simple graphical user interface (GUI) application for encrypting and decrypting images using the XOR encryption technique. The primary aim is to demonstrate how basic cryptographic operations can be applied to image files using Python and the Tkinter library.

**Features**:
Encrypt Image: Select a JPEG image and encrypt it using a user-provided numeric key.

Decrypt Image: Select an encrypted JPEG image and decrypt it using the same numeric key.

User-Friendly GUI: A simple and intuitive interface built with Tkinter for easy interaction.

How it Works
XOR Encryption: This technique is used for both encryption and decryption. By XORing each byte of the image with the provided key, the image is transformed into an encrypted format. The same operation with the same key is used to revert it to its original form.

File Handling: Users can select image files through the file dialog, and the application processes these files in place.
Usage

Install Dependencies: Ensure you have Python and Tkinter installed.
Run the Application: Execute the Python script to launch the GUI.

Encrypting an Image:
Enter a numeric key in the provided text box.
Click the "Encrypt Image" button and select the image to encrypt. 

Decrypting an Image:
Enter the same numeric key used for encryption.
Click the "Decrypt Image" button and select the encrypted image to decrypt.

Requirements: Python 3.x
Tkinter (comes pre-installed with standard Python distributions) 

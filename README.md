# Modified Caesar Cipher
 
# Modified Caesar Cipher GUI

This Python program implements a Modified Caesar Cipher Graphical User Interface (GUI) using the Tkinter library. The Modified Caesar Cipher is a simple encryption algorithm that shifts the letters in the input text based on a user-specified shift value.

## How it Works

1. The program displays a graphical window with input fields and buttons to interact with the Caesar Cipher.

2. The user can type their message in the "Type your message" entry widget.

3. The user selects the desired operation (encryption or decryption) by typing "encode" or "decode" in the "Type 'encode' to encrypt, 'decode' to decrypt" entry widget.

4. The user enters a numeric value representing the shift amount in the "Type the shift number" entry widget.

5. The user clicks the "Encrypt/Decrypt" button to trigger the encryption or decryption process.

6. The program performs the Caesar Cipher operation on the input text based on the user's selected operation and shift amount.

7. The result of the encryption or decryption is displayed in the "Result" label.

8. The user can restart the process by clicking the "Restart" button.

## Requirements

- Python 3.x
- Tkinter library (included in standard Python installations)

## How to Use

1. Run the `ModifiedCaesarCipher.py` script using Python.

2. A graphical window will appear, displaying the Modified Caesar Cipher GUI.

3. Enter your message in the "Type your message" entry widget.

4. Choose whether you want to "encode" or "decode" the message by typing the respective option in the "Type 'encode' to encrypt, 'decode' to decrypt" entry widget.

5. Enter a numeric value representing the shift amount (key) in the "Type the shift number" entry widget.

6. Click the "Encrypt/Decrypt" button to perform the Caesar Cipher operation.

7. The result of the encryption or decryption will be displayed in the "Result" label.

8. If you want to restart the process, click the "Restart" button.

## Note

- The Modified Caesar Cipher algorithm only shifts the letters of the English alphabet. Any other characters, such as numbers or special symbols, will remain unchanged.

- The shift amount is automatically adjusted to ensure it is within the range of 0 to 25, preventing large shift values that would produce inaccurate results.
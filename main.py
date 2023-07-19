import tkinter as tk
from tkinter import messagebox
from art import logo

class ModifiedCaesarCipher():

    def __init__(self):
        # Define the alphabet list
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.create_main_window()
        self.create_widgets()
        self.arrange_widgets()
        
    # Create the main window
    def create_main_window(self):
        self.root = tk.Tk()
        self.root.title("Modified Caesar Cipher")
        self.root.config(padx=40, pady=40)

    # Create widgets
    def create_widgets(self):
        self.logo_label = tk.Label(self.root, height=18, width=68, text=logo, font=("Courier", 20, "bold"))
        self.direction_label = tk.Label(self.root, text="Type 'encode' to encrypt, 'decode' to decrypt:")
        self.direction_entry = tk.Entry(self.root)
        self.text_label = tk.Label(self.root, text="Type your message:")
        self.text_entry = tk.Entry(self.root)
        self.shift_label = tk.Label(self.root, text="Type the shift number:")
        self.shift_entry = tk.Entry(self.root)
        self.result_label = tk.Label(self.root, text="Result: ")
        self.cipher_button = tk.Button(self.root, text="Encrypt/Decrypt", command=self.process_cipher)
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_program)
        self.trademark_label = tk.Label(self.root, text="Created by Deric C. San Andres", font=("Helvetica", 10, "italic"))
       

    # Arrange the widgets in their right positions
    def arrange_widgets(self):
        self.logo_label.grid(row=0, column=1, columnspan=2)
        self.direction_label.grid(row=1, column=0)
        self.direction_entry.grid(row=1, column=1, columnspan=2)
        self.text_label.grid(row=2, column=0)
        self.text_entry.grid(row=2, column=1, columnspan=2)
        self.shift_label.grid(row=3, column=0)
        self.shift_entry.grid(row=3, column=1, columnspan=2)
        self.result_label.grid(row=4, column=0, columnspan=3)
        self.cipher_button.grid(row=5, column=1)
        self.restart_button.grid(row=5, column=2)
        self.trademark_label.grid(row=6, column=2, columnspan=6)


        self.root.mainloop()

    # Caesar cipher function
    def caesar(self, start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char.isalpha():  # Check if the character is a letter
                position = self.alphabet.index(char)
                new_position = (position + shift_amount) % 26
                end_text += self.alphabet[new_position]
            else:
                end_text += char
        return end_text

    # Function to handle the button click
    def process_cipher(self):
        direction = self.direction_entry.get()
        text = self.text_entry.get().lower()
        shift = int(self.shift_entry.get()) % 26

        result = self.caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        self.result_label.config(text=f"Result: {result}")

    # Function to restart the program
    def restart_program(self):
        answer = messagebox.askquestion("Restart", "Do you want to go again?")
        if answer == "yes":
            self.direction_entry.delete(0, tk.END)
            self.text_entry.delete(0, tk.END)
            self.shift_entry.delete(0, tk.END)
            self.result_label.config(text="Result: ")
        else:
            self.root.quit()

# Create an instance of the ModifiedCaesarCipher class
if __name__ == "__main__":
    cipher = ModifiedCaesarCipher()

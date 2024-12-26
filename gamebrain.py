# coding: utf-8
import json
import tkinter
from tkinter import Tk, messagebox

INTER_WORDS = '/ '
INTER_LETTERS = ' '


class GameBrain(Tk):

    def __init__(self):
        super().__init__()

        with open("morse_json.json", "r", encoding='utf-8') as file:
            self.morse_dict = json.load(file)

        self.morse_message = ''
        self.missing_chars = []
        self.config(padx=50, pady=50)

        first_label = tkinter.Label(text="Please insert the text you'd like to convert to Morse code.")
        first_label.grid(column=0, row=0, columnspan=3)

        self.input_box = tkinter.Text(padx=10, pady=10, height=20)
        self.input_box.insert('end', "Please type here")
        self.input_box.grid(column=0, row=1, columnspan=3)

        second_label = tkinter.Label(text='\nYour morse code. Spaces are represented by a slash "/".')
        second_label.grid(column=0, row=2, columnspan=3)

        self.output_box = tkinter.Text(padx=10, pady=10, height=20)
        self.output_box.insert('end', ".--. .-.. . .- ... . / - -.-- .--. . / .... . .-. .")
        self.output_box.grid(column=0, row=3, columnspan=3)

        self.output_box.config(state='disabled')

        ghost_label = tkinter.Label(text="")
        ghost_label.grid(column=0, row=4, columnspan=3)

        convert_button = tkinter.Button(text='Convert', command=self.convert_text)
        convert_button.grid(column=0, row=5, columnspan=1)

        reset_button = tkinter.Button(text='Clear contents', command=self.clear_contents)
        reset_button.grid(column=2, row=5, columnspan=1)

        self.mainloop()

    def clear_contents(self):
        self.input_box.delete('1.0', 'end')
        self.output_box.config(state='normal')
        self.output_box.delete('1.0', 'end')
        self.output_box.config(state='disabled')

    def convert_text(self):
        self.morse_message = ''
        self.missing_chars = []

        if self.input_box.get('1.0', 'end') == '':
            self.output_box.delete('1.0', 'end')
            self.output_box.insert('1.0', '')
            return None
        else:
            text_input = self.input_box.get('1.0', 'end')
            for char in str(text_input):
                if char == ' ':
                    self.morse_message += INTER_WORDS
                elif char == '\n':
                    self.morse_message += '\n'
                else:
                    if char == '"':
                        char = 'QUOT'
                    morse_char = self.morse_dict.get(char.upper())
                    if morse_char is None:
                        self.missing_chars.append(char)
                        continue
                    else:
                        morse_char += INTER_LETTERS
                        self.morse_message += morse_char

            self.output_box.config(state='normal')
            self.output_box.delete('1.0', 'end')
            self.output_box.insert('end', self.morse_message)
            self.output_box.config(state='disabled')

            if len(self.missing_chars) > 0:
                print(self.missing_chars)
                missing_chars = set(self.missing_chars)
                messagebox.showerror('Unconverted items.',
                                     f'The following characters could not be converted to Morse:\n'
                                        f'{", ".join(missing_chars)}')

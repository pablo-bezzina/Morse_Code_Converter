from gamebrain import GameBrain
import pandas

this_game = GameBrain()

# 1. ONE-TIME ONLY CODE: covert csv into a dictionary, stored as a JSON at 'morse_json.json'.

'''df_morse = pandas.read_csv("morse_code.csv", encoding='utf-8-sig')

morse_dict = {}
for (index, row) in df_morse.iterrows():
    morse_dict.update({row.character: row.morse})

with open("morse_json.json", "w", encoding='utf-8') as file:
    json.dump(morse_dict, file, indent=4, ensure_ascii=False)'''


# 2. Working code: in gamebrain.py

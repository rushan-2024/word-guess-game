import tkinter as tk
import random

# ------------------- Word Bank by Difficulty -------------------
WORD_BANK = {
    "Easy": [
        'cat', 'dog', 'sun', 'moon', 'tree', 'book', 'fish', 'ball',
        'road', 'milk', 'cake', 'phone', 'clock', 'house', 'pen',
        'cup', 'hat', 'shoe', 'rain', 'wind', 'leaf', 'star',
        'lamp', 'door', 'bed', 'car', 'bus', 'toy', 'frog',
        'duck', 'bird', 'snow', 'sand', 'cake', 'rice', 'salt',
        'coin', 'map', 'ring', 'box', 'key'
    ],

    "Medium": [
        'computer', 'python', 'library', 'picture', 'diamond', 'journey',
        'monster', 'weather', 'holiday', 'camera', 'forest', 'island',
        'window', 'bottle', 'market', 'school', 'teacher', 'student',
        'garden', 'mirror', 'wallet', 'bridge', 'airport', 'station',
        'traffic', 'battery', 'speaker', 'charger', 'notebook',
        'backpack', 'helmet', 'painter', 'builder', 'manager',
        'captain', 'driver', 'farmer', 'doctor'
    ],

    "Hard": [
        'algorithm', 'mysterious', 'electricity', 'philosophy',
        'architecture', 'cybersecurity', 'revolution', 'environment',
        'psychology', 'communication', 'multiverse', 'engineering',
        'authentication', 'cryptography', 'infrastructure',
        'interpretation', 'configuration', 'implementation',
        'visualization', 'sustainability', 'transformation',
        'optimization', 'classification', 'serialization',
        'synchronization', 'parallelism', 'virtualization',
        'microservices', 'neuroscience', 'bioinformatics'
    ]
}

# ------------------- Game State -------------------
word = ""
guesses = []
turns = 0
hint_used = False
wins = 0
losses = 0

# ------------------- GUI -------------------
root = tk.Tk()
root.title("Word Guessing Game")
root.geometry("450x420")
root.resizable(False, False)

# ------------------- Functions -------------------
def start_game():
    global word, guesses, turns, hint_used
    difficulty = difficulty_var.get()
    word = random.choice(WORD_BANK[difficulty])
    guesses = []
    hint_used = False

    # 🔥 Always reset turns to 12
    turns = 12

    entry.config(state="normal")
    update_display()
    feedback_label.config(text="")
    status_label.config(text="")
    turns_label.config(text=f"Turns left: {turns}")
    hint_btn.config(state="normal")


def update_display():
    shown = ""
    failed = 0
    for char in word:
        if char in guesses:
            shown += char + " "
        else:
            shown += "_ "
            failed += 1
    display_word.config(text=shown.strip())

    if failed == 0:
        end_game(win=True)

def make_guess():
    global turns
    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if not guess or len(guess) != 1 or not guess.isalpha():
        feedback_label.config(text="Enter a single valid letter!", fg="red")
        return

    if guess in guesses:
        feedback_label.config(text="Already guessed!", fg="orange")
        return

    guesses.append(guess)

    if guess not in word:
        turns -= 1
        feedback_label.config(text=f"Wrong guess: '{guess}'", fg="red")
    else:
        feedback_label.config(text=f"Good guess: '{guess}'", fg="green")

    turns_label.config(text=f"Turns left: {turns}")
    update_display()

    if turns == 0:
        end_game(win=False)

def use_hint():
    global hint_used
    if hint_used:
        return

    hidden_letters = [c for c in word if c not in guesses]
    if hidden_letters:
        letter = random.choice(hidden_letters)
        guesses.append(letter)
        hint_used = True
        hint_btn.config(state="disabled")
        feedback_label.config(text=f"Hint used! Letter revealed: '{letter}'", fg="blue")
        update_display()

def end_game(win):
    global wins, losses
    entry.config(state="disabled")
    hint_btn.config(state="disabled")

    if win:
        wins += 1
        status_label.config(text="🎉 You Win!", fg="green")
    else:
        losses += 1
        status_label.config(text=f"😞 You Lose! Word was: {word}", fg="red")

    score_label.config(text=f"Wins: {wins} | Losses: {losses}")

def restart_game():
    start_game()

# ------------------- UI Elements -------------------
tk.Label(root, text="🎯 Word Guessing Game", font=("Arial", 18, "bold")).pack(pady=10)

# Difficulty
difficulty_var = tk.StringVar(value="Easy")
tk.Label(root, text="Select Difficulty:", font=("Arial", 12)).pack()
tk.OptionMenu(root, difficulty_var, "Easy", "Medium", "Hard").pack(pady=5)

# Status
status_label = tk.Label(root, text="", font=("Arial", 14))
status_label.pack(pady=5)

display_word = tk.Label(root, text="", font=("Arial", 20))
display_word.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

feedback_label = tk.Label(root, text="", font=("Arial", 12))
feedback_label.pack()

turns_label = tk.Label(root, text="", font=("Arial", 12))
turns_label.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Guess", width=10, command=make_guess).grid(row=0, column=0, padx=5)
hint_btn = tk.Button(btn_frame, text="Hint", width=10, command=use_hint)
hint_btn.grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Restart", width=10, command=restart_game).grid(row=0, column=2, padx=5)

# Score
score_label = tk.Label(root, text="Wins: 0 | Losses: 0", font=("Arial", 12, "bold"))
score_label.pack(pady=10)

# ------------------- Start First Game -------------------
start_game()
root.mainloop()

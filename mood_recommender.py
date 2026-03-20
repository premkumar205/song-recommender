import random
import webbrowser
import tkinter as tk
from tkinter import messagebox

# Mood-to-song mapping 
songs = {
    "happy": [
        ("Happy", "Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
        ("Butta Bomma", "Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=2Vv-BfVoq4g"),
        ("Darshana", "Darling", "https://www.youtube.com/watch?v=nvD-GkVflHg"),
        ("Uppena Title Song", "Uppena", "https://www.youtube.com/watch?v=H3mtROiQfnU")
    ],
    "sad": [
        ("naa pranama", "Adele", "https://www.youtube.com/watch?v=c3QLGiYrnHo&list=RDc3QLGiYrnHo&start_radio=1"),
        ("Samajavaragamana", "Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=lk_BzK6-LIM"),
        ("Nuvvunte Naa Jathaga", "I", "https://www.youtube.com/watch?v=nhfO0Wk3j1A"),
        ("Ye Chota Nuvvunna", "A Aa", "https://www.youtube.com/watch?v=hQv1vw9j5RE")
    ],
    "relaxed": [
        ("Weightless", "Marconi Union", "https://www.youtube.com/watch?v=UfcAVejslrU"),
        ("Priyathama Priyathama", "Majili", "https://www.youtube.com/watch?v=d3mJjDwE1lU"),
        ("Inkem Inkem Inkem Kaavaale", "Geetha Govindam", "https://www.youtube.com/watch?v=NIJtqHcl3Xc"),
        ("Kal Ho Naa Ho", "Shankar-Ehsaan-Loy", "https://www.youtube.com/watch?v=5bNE-5Tv_YM")
    ],
    "energetic": [
        ("Believer", "Imagine Dragons", "https://www.youtube.com/watch?v=7wtfhZwyrcc"),
        ("Ramuloo Ramulaa", "Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=ez1xkVlDkR4"),
        ("Seeti Maar", "DJ", "https://www.youtube.com/watch?v=R2vXbFp5C9o"),
        ("Badtameez Dil", "Yeh Jawaani Hai Deewani", "https://www.youtube.com/watch?v=II2EO3Nw4m0")
    ]
}

# Function to pick and open a song based on mood
def recommend_song(mood_choice):
    mood_choice = mood_choice.strip().lower()
    if mood_choice in songs:
        song = random.choice(songs[mood_choice])
        messagebox.showinfo("Song Recommendation", f"🎵 I recommend: '{song[0]}' by {song[1]}")
        webbrowser.open(song[2])
    else:
        messagebox.showwarning("Mood Not Found", "Sorry, we don't have songs for that mood yet.")

# GUI Setup
root = tk.Tk()
root.title("Mood-Based Song Recommender")
root.geometry("400x200")
root.resizable(False, False)

label = tk.Label(root, text="Select your mood:", font=("Arial", 14))
label.pack(pady=20)

# Create buttons for each mood
for mood_name in songs.keys():
    btn = tk.Button(root, text=mood_name.capitalize(), width=15, font=("Arial", 12),
                    command=lambda m=mood_name: recommend_song(m))
    btn.pack(pady=5)

root.mainloop()

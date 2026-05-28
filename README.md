# Snake Clash 🚀🐍

An arcade-style, space-themed Snake game built using Python and the `pygame` library. Guide your snake through space, consume different types of food to increase your score, avoid crashing into yourself or the walls, and aim for the ultimate high score!

---

# 🌟 Features

## Diverse Food Types

- ⚫ **Normal Food (Black)**  
  Regular food that awards **10 points**.

- 🔴 **Bonus Food (Red)**  
  Rare item that awards **50 points**.

- 🔵 **Slow Food (Blue)**  
  Slows down the game speed for easier maneuvering.

---

## 🎨 Visual Highlights

- Smooth background visuals
- Distinct snake colors
  - 🟢 Green snake head with eyes
  - 🟡 Yellow snake body
- Rounded borders for cleaner graphics

---

## 🔊 Sound Effects

- Eating sound effect
- Game over sound effect

---

## 💾 Persistent Tracking

- High-score system using `hiscore.txt`

---

## 🎮 Gameplay Functions

- Pause and resume support
- Instant restart after game over

---

# 🕹️ Controls

| Key | Action |
|------|--------|
| `SPACEBAR` | Start the game |
| `ARROW KEYS` | Move the snake |
| `P` | Pause / Resume |
| `ENTER` | Restart after Game Over |

---

# 🛠️ Requirements & Installation

Before running the game, make sure Python is installed on your system.

You also need the `pygame` library.

## 📦 Install Dependencies

Open terminal or command prompt and run:

```bash
pip install pygame
```

---

# 📁 Assets Needed

Make sure the following files are present in the **root directory** alongside your Python script:

- `snake_bg.jpg` — Background image
- `eat.mp3` — Sound played when eating food
- `game_over.mp3` — Sound played on losing

---

# 🚀 How to Run the Game

1. Clone or download this repository
2. Place all required asset files in the project folder
3. Run the game using:

```bash
python snakes.py
```

---

# 🧠 Game Logic

- Snake grows after eating food
- Collision with walls ends the game
- Collision with itself ends the game
- Different foods provide different gameplay effects

---

# 🛠️ Built With

- Python
- Pygame

---

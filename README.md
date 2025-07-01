
# 🎓 Progression Outcome Predictor
---

## 📖 Introduction

This is a Python-based program that predicts progression outcomes based on inputted credit values for **Pass**, **Defer**, and **Fail**. 
Based on the inputs, the program determines whether a student:

- ✅ Progresses
- 🚩 Progresses (module trailer)
- 🔄 Requires module retrieval
- ❌ Is excluded

It also generates a histogram visualization of the progression outcomes using the `graphics.py` library. It includes input validation, multiple data handling, and file handling for saving and loading progression data.

---

## ✨ Features

- ✔️ Input validation (integer check, range check, total check)
- ✔️ Handles both single and multiple progression checks
- ✔️ Stores progression data in nested lists
- ✔️ Generates a **graphical histogram** using `graphics.py`
- ✔️ Saves progression outcomes to a text file and retrieves them
- ✔️ User-friendly interface with clear prompts
- ✔️ Structured with user-defined functions

---

## 🚀 How to Run

### Requirements:
- Python 3.x
- `graphics.py` library (included with the project)

### Steps:
1. Download or clone this repository:
   ```
   git clone https://github.com/PoornaManakal/Grading-System.git
2. Place `graphics.py` in the same directory as the main Python file (if not already included).
3. Run the Python file:
   ```
   python main.py
   ```
4. Follow the prompts:
   - Enter `0` for single input
   - Enter `1` for multiple inputs with histogram and file handling

---

##  Program Structure

| File                  | Description                                  |
|-----------------------|----------------------------------------------|
| `main.py`             | Main Python program                         |
| `graphics.py`         | Graphics library for histogram visualization|
| `Programme_Inputs.txt`| Auto-generated file storing progression data |
| `README.md`           | Project documentation                       |

---

##  Example Run

```bash
Enter '0' for single input or '1' for multiple inputs : 1

Please Enter your credit at pass : 100
Please Enter your credit at defer : 20
Please Enter your credit at fail : 0
Progress (module trailer)

Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view result : y

...

[When 'q' is entered, a histogram is displayed]
```

✔️ After quitting, the program:
- Displays all progression outcomes from this session.
- Saves the data to `Programme_Inputs.txt`.
- Reads from the file and prints the content.


# 📱 Robust Tech Store Inventory Tracker

A professional-grade Python automation script designed to log retail inventory with high-level error handling. 

 **Project Overview**
In a real-world retail environment, user input is unpredictable. This project demonstrates how to build a persistent, crash-resistant interface that ensures data integrity even when a user makes mistakes.

## ⚙️ Core Logic & Technical Features
* **Robust Input Validation:** Implements a conditional check (`if not item:`) to immediately catch empty inputs. This prevents the system from saving "blank" records if the user accidentally presses Enter.
* **Persistent Loop Control:** Utilizes a `while True` loop to create a continuous session, allowing the user to log multiple items without restarting the program.
* **Flexible Exit Protocol:** Employs a membership check against a list `['finish', 'Finish', 'FINISH']`. This handles case-sensitivity, ensuring the program closes gracefully regardless of how the user types the exit command.
* **User Feedback System:** Provides immediate console feedback to the user, confirming successful entries or flagging errors in real-time.

## 🚀 How to Run
1. Ensure you have **Python 3.x** installed.
2. Clone this repository.
3. Run `python inventory_tracker.py` in your terminal.
4. Log your items (e.g., iPhone 15, MacBook) and type `finish` to exit.

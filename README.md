# 📊 Personal Ledger & Hotkey Dashboard

A lightweight, background-running financial tracker built in Python. This tool allows users to log daily financial transactions seamlessly from the terminal, 
automatically timestamps them, and provides on-demand, hotkey-triggered graphical summaries using native OS listeners.

## 🚀 Features
* **Continuous Logging:** A staging terminal that stays active in the background.
* **Smart Data Parsing:** Handles both positive (Income) and negative (Expenses) numerical values natively.
* **Automated Timestamps:** Integrates Python's `datetime` module to stamp every entry automatically.
* **Dynamic Architecture:** Utilizes nested dictionaries to auto-generate and sort data by month without hardcoding.
* **Global Hotkeys:** Uses the `keyboard` module to listen for hardware triggers even when the terminal is minimized.
  * Press `F2` -> View Lifetime Category Balance
  * Press `F3` -> View Monthly Time-Series Breakdown

## 📥 Download & Use (For Standard Users)
You do not need Python or any coding experience to use this app!
1. Go to the [Releases](#) tab on the right side of this GitHub page.
2. Download the latest `expense_tracker.exe` file.
3. Double-click the file to run the dashboard immediately. 

## 🛠️ Build from Source (For Developers)
If you want to view or modify the code:
1. Clone the repository.
2. Install the hardware listener dependencies:
   `pip install -r requirements.txt`
3. Run the script via terminal:
   `python expense_tracker.py`

# 👩🏻‍💻 TypeSim – Secure Typing Tool

[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
![Version](https://img.shields.io/badge/version-2.1-brightgreen)

## ✨ Introduction

**TypeSim** is a cross-platform GUI tool that simulates human-like typing behavior, helping you bypass copy-paste restrictions by typing your text automatically.

> 🧠 Ideal for restricted environments like VMs, remote desktops, or software that blocks clipboard operations.

## 📦 What's Inside the Repo?

✅ No installation required  
⚙️ Fully standalone build  
🖥️ Works out-of-the-box on Windows  
🔒 No dependencies

---

## 🛠️ First-Time Setup (Important)

When you launch **TypeSim.exe** for the first time, Windows Defender SmartScreen may block it, as it's from an unknown publisher.

<p align="center">
  <img src="assets/protect1.png" width="400" />
  <br/>
  <strong>Step 1:</strong> Click <code>More Info</code>
</p>

<p align="center">
  <img src="assets/protect2.png" width="400" />
  <br/>
  <strong>Step 2:</strong> Click <code>Run Anyway</code>
</p>

> ✅ After that, it runs normally. Windows remembers your choice.

---

## 🖥️ Using TypeSim – GUI Breakdown

<p align="center">
  <img src="assets/interface.png" width="450"/>
</p>

### Features:
- 💡 **Load Text from File**: Import a list of lines to type.
- 🎯 **Text Area**: Type or paste content manually, one line per entry.
- 🧠 **Dark Mode Toggle**: Enable/disable dark UI.
- 🧩 **Start Typing**: Simulates typing wherever your cursor is placed.

> Example Text:
This text will be typed automatically.
Works in restricted environments.
No copy-paste required.
Click Start & Just position your cursor!
Make sure to visit my GitHub page and drop a star.

---

## 📎 How It Works

- Uses `pyautogui` to simulate keypresses.
- Works on most text fields including terminals, IDEs, editors, etc.
- Can bypass **copy-paste disabled** areas.

---

## 🧠 Tips

- Make sure the cursor is **focused in a text field** before clicking **Start Typing**.
- To stop mid-way, press `Esc` or move the cursor out.
- You can add delays or tweak behavior by editing the source before building.
---
## 📁 Developer Notes

- Built using: `Python`, `Tkinter`, `PyInstaller`
- Works on: **Windows**
- OnProgress: **Linux**
---
## 🔐 Disclaimer
> This tool is for educational and productivity purposes only. Please use it responsibly and ethically.
---
## ⭐ Like it? Support by Giving a Star!
[![GitHub Repo stars](https://img.shields.io/github/stars/Audi14-2005/TypeSim?style=social)](https://github.com/Audi14-2005/TypeSim)
---

## 👨‍💻 Author

Created by **Audi14**  
[GitHub](https://github.com/Audi14-2005) | [LinkedIn](https://www.linkedin.com/in/monic-auditya-a-b8bb68295/)

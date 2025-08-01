import pyautogui
import time
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import webbrowser

def open_github():
    webbrowser.open("https://github.com/Audi14-2005/TypeSim.git")

def toggle_theme():
    # Toggle between dark and light modes
    if mode_switch.instate(["selected"]):
        # Dark Mode
        root.tk_setPalette(background='#2c3e50', foreground='#ecf0f1')
        style.configure('.', background='#2c3e50', foreground='#ecf0f1')
        style.configure('TFrame', background='#2c3e50')
        style.configure('TLabel', background='#2c3e50', foreground='#ecf0f1')
        style.configure('TButton', background='#16a085', foreground='white')
        style.map('TButton', background=[('active', '#1abc9c')])
        style.configure('Header.TLabel', background='#2c3e50', foreground='#ecf0f1')
        style.configure('Credits.TLabel', background='#2c3e50', foreground='#bdc3c7')
        style.configure('Link.TLabel', background='#2c3e50', foreground='#3498db')
        style.configure('TCheckbutton', background='#2c3e50', foreground='#ecf0f1')
        style.configure('TLabelFrame', background='#2c3e50', foreground='#ecf0f1')
        text_area.configure(bg='#34495e', fg='#ecf0f1', insertbackground='white')
        file_button.configure(style='TButton')
        mode_switch.configure(text='☀️ Light Mode')
    else:
        # Light Mode
        root.tk_setPalette(background='#f5f5f5', foreground='#2c3e50')
        style.configure('.', background='#f5f5f5', foreground='#2c3e50')
        style.configure('TFrame', background='#f5f5f5')
        style.configure('TLabel', background='#f5f5f5', foreground='#2c3e50')
        style.configure('TButton', background='#4CAF50', foreground='white')
        style.map('TButton', background=[('active', '#45a049')])
        style.configure('Header.TLabel', background='#f5f5f5', foreground='#2c3e50')
        style.configure('Credits.TLabel', background='#f5f5f5', foreground='#555555')
        style.configure('Link.TLabel', background='#f5f5f5', foreground='#0066cc')
        style.configure('TCheckbutton', background='#f5f5f5', foreground='#2c3e50')
        style.configure('TLabelFrame', background='#f5f5f5', foreground='#2c3e50')
        text_area.configure(bg='white', fg='black', insertbackground='black')
        file_button.configure(style='TButton')
        mode_switch.configure(text='🌙 Dark Mode')

def load_from_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, content)
        messagebox.showinfo("Success", f"Loaded content from {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load file:\n{str(e)}")

def start_typing():
    input_text = text_area.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Warning", "Please enter some statements.")
        return

    statements = [line.strip() for line in input_text.splitlines() if line.strip()]
    
    if not statements:
        messagebox.showwarning("Warning", "No valid statements found.")
        return

    confirm = messagebox.askyesno("Confirm", 
                                 f"Ready to type {len(statements)} statements?\nSwitch to target window now.")
    if not confirm:
        return
        
    root.withdraw()
    time.sleep(2)
    
    def type_and_send(statement):
        pyautogui.typewrite(statement, interval=0.05)
        pyautogui.press('enter')
        time.sleep(1)

    for statement in statements:
        type_and_send(statement)

    messagebox.showinfo("Done", f"✅ Successfully typed {len(statements)} statements.")
    root.destroy()

# GUI Setup
root = tk.Tk()

import sys
import os

# Set icon for the window (title bar & taskbar)
if getattr(sys, 'frozen', False):
    icon_path = os.path.join(sys._MEIPASS, "logo.ico")
else:
    icon_path = os.path.abspath("logo.ico")

root.iconbitmap(icon_path)



root.title("TypeSim - Secure Typing Tool")
root.geometry("550x650")
root.resizable(True, True)
root.attributes('-topmost', True)

# Modern theme and styling
style = ttk.Style()
style.theme_use('clam')

# Main container
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Header with theme toggle
header_frame = ttk.Frame(main_frame)
header_frame.pack(fill=tk.X, pady=(0, 10))

title_frame = ttk.Frame(header_frame)
title_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
ttk.Label(title_frame, text="Secure Typing Tool", 
          style='Header.TLabel', font=('Segoe UI', 12, 'bold')).pack(anchor='w')

# Theme toggle switch
switch_frame = ttk.Frame(header_frame)
switch_frame.pack(side=tk.RIGHT, fill=tk.Y)
mode_switch = ttk.Checkbutton(
    switch_frame, 
    text="🌙 Dark Mode", 
    style='Switch.TCheckbutton',
    command=toggle_theme
)
mode_switch.pack(padx=5)

# Description
ttk.Label(main_frame, 
          text="Bypass copy-paste restrictions with simulated typing",
          style='Credits.TLabel').pack(pady=(0, 10))

# File loading section
file_frame = ttk.Frame(main_frame)
file_frame.pack(fill=tk.X, pady=(0, 10))
file_button = ttk.Button(
    file_frame, 
    text="📁 Load Text from File", 
    command=load_from_file,
    style='TButton'
)
file_button.pack(fill=tk.X, ipady=5)

# Text area section
text_frame = ttk.LabelFrame(main_frame, text="Enter your text (one line per entry):", padding=10)
text_frame.pack(fill=tk.BOTH, expand=True)

# Scrollable text area
text_container = ttk.Frame(text_frame)
text_container.pack(fill=tk.BOTH, expand=True)

text_area = tk.Text(text_container, height=12, font=('Consolas', 10), wrap=tk.WORD)
text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(text_container, command=text_area.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scrollbar.set)

# Sample text
sample_text = """This text will be typed automatically.
Works in restricted environments.
No copy-paste required.
Click Start & Just position your cursor!
Make sure to visit my GitHub page and drop a star.
"""
text_area.insert(tk.END, sample_text)

# Button frame
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill=tk.X, pady=15)

start_button = ttk.Button(button_frame, text="START TYPING", 
                         command=start_typing, style='TButton')
start_button.pack(ipadx=20, ipady=8)

# Footer Frame (Full Width)
footer_frame = ttk.Frame(main_frame)
footer_frame.pack(fill=tk.X, pady=(10, 0))

# Left side content
left_footer = ttk.Frame(footer_frame)
left_footer.pack(side=tk.LEFT)

ttk.Label(left_footer, text="Powered by:", style='Credits.TLabel').pack(side=tk.LEFT)
ttk.Label(left_footer, text="🐍 Python", style='Credits.TLabel').pack(side=tk.LEFT, padx=5)
ttk.Label(left_footer, text="| Created By: Audi14", style='Credits.TLabel').pack(side=tk.LEFT, padx=5)

# Create style for link
style.configure("Link.TLabel", foreground="blue", font=("Segoe UI", 10, "underline"))

# Create GitHub label
github_link = ttk.Label(left_footer, text="GitHub", style="Link.TLabel", cursor="hand2")
github_link.pack(side=tk.LEFT, padx=5)

# Bind hover events
def on_enter(e):
    github_link.configure(foreground="#3939E1")  # bright blue

def on_leave(e):
    github_link.configure(foreground="black")  # reset to original

github_link.bind("<Enter>", on_enter)
github_link.bind("<Leave>", on_leave)
github_link.bind("<Button-1>", lambda e: open_github())
# Right side content
ttk.Label(footer_frame, text="v2.1", style='Credits.TLabel').pack(side=tk.RIGHT)

# Initialize theme
toggle_theme()

root.mainloop()

import os
import platform

separator = ";" if platform.system() == "Windows" else ":"
os.system(f'pyinstaller --noconfirm --onefile --windowed --icon=logo.ico --add-data="logo.ico{separator}." TypeSim-v2.py')

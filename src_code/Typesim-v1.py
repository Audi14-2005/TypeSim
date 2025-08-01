# MIT License
# Copyright (c) 2025 Monic Auditya.A (Audi)
#
# See the LICENSE file in the root of this project for license information.
import pyautogui
import random
import time
statements = [
"""
    "Hello everyone! How's it going?",
    "Just wanted this to be autotyped",
"""
]
print("Starting in 7 seconds... Switch to desired type area now!.")
time.sleep(7)
def type_and_send(statement):
    pyautogui.typewrite(statement, interval=0.05)  # Type slower for realism
    pyautogui.press('enter')  
    time.sleep(1)
while statements:
    statement = random.choice(statements)
    statements.remove(statement)
    type_and_send(statement)
    time.sleep(1) 

print("✅ All statements Typed.")
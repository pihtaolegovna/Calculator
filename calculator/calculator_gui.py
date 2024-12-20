import os
import tkinter as tk
from tkinter import messagebox

SETTINGS_PATH = "/settings/settings.txt"
VOLUME_PATH = "/data/results.txt"

def load_config():
    config = {}
    if os.path.exists(SETTINGS_PATH):
        with open(SETTINGS_PATH, "r") as settings_file:
            for line in settings_file:
                key, value = line.strip().split(": ")
                config[key] = value.strip()
    return config

def save_result(expression, result):
    if config.get("auto_save", "true").lower() == "true":
        with open(VOLUME_PATH, "a") as results_file:
            results_file.write(f"{expression} = {result}\n")

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        label_result["text"] = f"Результат: {result}"
        save_result(expression, result)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Неверное выражение: {e}")

config = load_config()

# Создаем GUI
app = tk.Tk()
app.title("Calculator")
app.geometry("300x200")

# Ввод выражения
entry = tk.Entry(app, width=25)
entry.pack(pady=10)

# Кнопка вычисления
button_calculate = tk.Button(app, text="Вычислить", command=calculate)
button_calculate.pack(pady=5)

# Отображение результата
label_result = tk.Label(app, text="Результат:")
label_result.pack(pady=10)

# Настройка темы
if config.get("theme") == "dark":
    app.configure(bg="black")
    label_result.configure(bg="black", fg="white")

app.mainloop()

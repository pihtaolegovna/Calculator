import os
import tkinter as tk

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

def load_results():
    if os.path.exists(VOLUME_PATH):
        with open(VOLUME_PATH, "r") as results_file:
            return results_file.read()
    else:
        return "Результатов пока нет."

def refresh_results():
    results = load_results()
    text_results.delete(1.0, tk.END)
    text_results.insert(tk.END, results)

config = load_config()

# Создаем GUI
app = tk.Tk()
app.title("Viewer")
app.geometry("400x300")

# Настройка темы
if config.get("theme") == "dark":
    app.configure(bg="black")

# Текстовое поле для результатов
text_results = tk.Text(app, wrap=tk.WORD)
text_results.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Кнопка обновления
button_refresh = tk.Button(app, text="Обновить", command=refresh_results)
button_refresh.pack(pady=5)

# Загрузка и отображение результатов
refresh_results()

app.mainloop()

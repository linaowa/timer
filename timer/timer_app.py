import tkinter as tk
from tkinter import messagebox
import time


class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Таймер")

        self.label_time = tk.Label(self.master, text="Введите время (в секундах):")
        self.label_time.pack()

        self.entry_time = tk.Entry(self.master)
        self.entry_time.pack()

        self.start_button = tk.Button(self.master, text="Старт", command=self.start_timer)
        self.start_button.pack()

        self.timer_label = tk.Label(self.master, text="", font=("Helvetica", 48))
        self.timer_label.pack()

        self.is_running = False
        self.end_time = None

    def start_timer(self):
        if not self.is_running:
            try:
                duration = int(self.entry_time.get())
                if duration > 0:
                    self.end_time = time.time() + duration
                    self.is_running = True
                    self.update_timer()
                else:
                    messagebox.showwarning("Ошибка", "Введите положительное число секунд")
            except ValueError:
                messagebox.showwarning("Ошибка", "Введите число в секундах")

    def update_timer(self):
        if self.is_running:
            remaining_time = self.end_time - time.time()
            if remaining_time <= 0:
                self.is_running = False
                self.timer_label.config(text="Время вышло!")
            else:
                minutes, seconds = divmod(int(remaining_time), 60)
                self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
                self.master.after(1000, self.update_timer)


def main():
    root = tk.Tk()
    timer_app = TimerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
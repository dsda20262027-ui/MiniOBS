import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import time

class MiniOBS(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mini OBS Studio")
        self.geometry("1000x650")
        self.minsize(820, 520)
        self.configure(bg="#171717")
        self.recording = False
        self.started = 0
        self.timer_job = None
        self.output = Path.home() / "Videos" / "MiniOBS"
        self.output.mkdir(parents=True, exist_ok=True)
        self.build_ui()

    def build_ui(self):
        top = tk.Frame(self, bg="#242424", height=50)
        top.pack(fill="x")
        tk.Label(top, text="● Mini OBS Studio", fg="white", bg="#242424",
                 font=("Segoe UI", 16, "bold")).pack(side="left", padx=16, pady=10)
        tk.Button(top, text="Настройки", command=self.settings,
                  bg="#333", fg="white", relief="flat").pack(side="right", padx=12)

        main = tk.Frame(self, bg="#171717")
        main.pack(fill="both", expand=True, padx=12, pady=12)

        preview = tk.Frame(main, bg="#090909", highlightbackground="#444",
                           highlightthickness=1)
        preview.pack(side="left", fill="both", expand=True, padx=(0, 10))
        tk.Label(preview, text="ПРЕДПРОСМОТР", fg="#777", bg="#090909",
                 font=("Segoe UI", 10, "bold")).place(x=12, y=10)
        self.preview = tk.Label(preview, text="Источник не выбран",
                                fg="#888", bg="#090909", font=("Segoe UI", 20))
        self.preview.place(relx=.5, rely=.5, anchor="center")

        side = tk.Frame(main, bg="#202020", width=280)
        side.pack(side="right", fill="y")
        side.pack_propagate(False)

        tk.Label(side, text="Источники", fg="white", bg="#202020",
                 font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=14, pady=(14, 7))
        self.sources = tk.Listbox(side, bg="#151515", fg="#ddd",
                                  selectbackground="#444", borderwidth=0)
        self.sources.pack(fill="x", padx=12)
        for x in ("Display Capture", "Window Capture", "Microphone"):
            self.sources.insert("end", x)

        tk.Label(side, text="Управление", fg="white", bg="#202020",
                 font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=14, pady=(22, 7))

        self.status = tk.Label(side, text="● Готов", fg="#8fd18f", bg="#202020")
        self.status.pack(anchor="w", padx=14)

        self.clock = tk.Label(side, text="00:00:00", fg="white", bg="#202020",
                              font=("Consolas", 20, "bold"))
        self.clock.pack(pady=10)

        self.record_btn = tk.Button(
            side, text="● Начать запись", command=self.toggle_recording,
            bg="#b3261e", fg="white", activebackground="#d43a30",
            activeforeground="white", relief="flat",
            font=("Segoe UI", 11, "bold"), pady=10)
        self.record_btn.pack(fill="x", padx=14, pady=5)

        tk.Button(side, text="📁 Папка записи", command=self.choose_folder,
                  bg="#333", fg="white", relief="flat", pady=9).pack(
                      fill="x", padx=14, pady=5)

        tk.Button(side, text="🖥 Добавить экран", command=self.add_display,
                  bg="#333", fg="white", relief="flat", pady=8).pack(
                      fill="x", padx=14, pady=3)
        tk.Button(side, text="🪟 Добавить окно", command=self.add_window,
                  bg="#333", fg="white", relief="flat", pady=8).pack(
                      fill="x", padx=14, pady=3)

    def add_display(self):
        self.sources.insert("end", "Display Capture")
        self.preview.config(text="🖥 Захват экрана\n\nПредпросмотр")

    def add_window(self):
        self.sources.insert("end", "Window Capture")
        self.preview.config(text="🪟 Захват окна\n\nПредпросмотр")

    def choose_folder(self):
        folder = filedialog.askdirectory(initialdir=str(self.output))
        if folder:
            self.output = Path(folder)
            self.status.config(text=f"● Папка: {self.output.name}")

    def toggle_recording(self):
        if self.recording:
            self.recording = False
            if self.timer_job:
                self.after_cancel(self.timer_job)
            self.record_btn.config(text="● Начать запись", bg="#b3261e")
            self.status.config(text="● Готов", fg="#8fd18f")
            return

        self.recording = True
        self.started = time.time()
        self.record_btn.config(text="■ Остановить", bg="#444")
        self.status.config(text="● Запись", fg="#ff7777")
        self.update_timer()

    def update_timer(self):
        if not self.recording:
            return
        elapsed = int(time.time() - self.started)
        h, rem = divmod(elapsed, 3600)
        m, s = divmod(rem, 60)
        self.clock.config(text=f"{h:02}:{m:02}:{s:02}")
        self.timer_job = self.after(500, self.update_timer)

    def settings(self):
        messagebox.showinfo("Mini OBS Studio",
                            f"Папка записи:\n{self.output}\n\n"
                            "Это первая версия интерфейса Mini OBS Studio.")

if __name__ == "__main__":
    MiniOBS().mainloop()

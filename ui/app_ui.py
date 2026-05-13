import tkinter as tk
import subprocess
import sys
import os


class GestureAIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GestureAI - Sign Language Recognition")
        self.root.geometry("900x550")
        self.root.configure(bg="#f4f6f8")

        self.create_ui()

    def create_ui(self):
        title = tk.Label(
            self.root,
            text="GestureAI",
            font=("Arial", 30, "bold"),
            bg="#f4f6f8",
            fg="#1f2937"
        )
        title.pack(pady=20)

        subtitle = tk.Label(
            self.root,
            text="Real-Time Sign Language Recognition System",
            font=("Arial", 14),
            bg="#f4f6f8",
            fg="#4b5563"
        )
        subtitle.pack()

        card_frame = tk.Frame(self.root, bg="#f4f6f8")
        card_frame.pack(pady=40)

        self.create_card(card_frame, "Hand Detection", "Completed ✅", 0, 0)
        self.create_card(card_frame, "Data Collection", " Done ✅", 0, 1)
        self.create_card(card_frame, "Model Training", "Completed ✅", 1, 0)
        self.create_card(card_frame, "Prediction", "Working ✅", 1, 1)

        btn_frame = tk.Frame(self.root, bg="#f4f6f8")
        btn_frame.pack(pady=20)

        start_btn = tk.Button(
            btn_frame,
            text="Start Prediction",
            font=("Arial", 14, "bold"),
            bg="#2563eb",
            fg="white",
            width=18,
            height=2,
            command=self.start_prediction
        )
        start_btn.grid(row=0, column=0, padx=15)

        exit_btn = tk.Button(
            btn_frame,
            text="Exit",
            font=("Arial", 14, "bold"),
            bg="#dc2626",
            fg="white",
            width=18,
            height=2,
            command=self.root.destroy
        )
        exit_btn.grid(row=0, column=1, padx=15)

    def create_card(self, parent, title, value, row, col):
        card = tk.Frame(parent, bg="white", width=300, height=110)
        card.grid(row=row, column=col, padx=20, pady=15)
        card.grid_propagate(False)

        tk.Label(
            card,
            text=title,
            font=("Arial", 15, "bold"),
            bg="white",
            fg="#111827"
        ).pack(pady=(20, 5))

        tk.Label(
            card,
            text=value,
            font=("Arial", 13),
            bg="white",
            fg="#16a34a"
        ).pack()

    def start_prediction(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        predict_file = os.path.join(project_root, "predict.py")

        subprocess.Popen(
            [sys.executable, predict_file],
            cwd=project_root
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = GestureAIApp(root)
    root.mainloop()
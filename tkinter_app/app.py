import sys
from pathlib import Path
sys.path.insert(0, r"d:\3rd semester project DNA")

import tkinter as tk
from tkinter import scrolledtext
from algorithms.kmp import kmp_search
from algorithms.suffix_array import build_suffix_array, suffix_search
from algorithms.mutation import detect_mutations
from algorithms.alignment import needleman_wunsch
from ml.mutation_predictor import predict_mutation_probability
from utils.plotter import plot_mutations
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

BG="#020617"; FG="#e5e7eb"; ACC="#38bdf8"

root=tk.Tk()
root.title("DNA Sequence Analyzer")
root.geometry("1100x750")
root.configure(bg=BG)

# Canvas with scrollbar
canvas=tk.Canvas(root,bg=BG,highlightthickness=0)
scroll=tk.Scrollbar(root,command=canvas.yview,bg=BG)

# Frame that will hold all content
frame=tk.Frame(canvas,bg=BG)

# Bind the frame to update scrollregion when size changes
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

# Create window in canvas - centered horizontally
canvas_window = canvas.create_window((550,0),window=frame,anchor="n")

# Recenter the frame when canvas is resized
def on_canvas_configure(event):
    canvas.itemconfig(canvas_window, width=event.width)

canvas.bind("<Configure>", on_canvas_configure)

canvas.config(yscrollcommand=scroll.set)

canvas.pack(side="left",fill="both",expand=True)
scroll.pack(side="right",fill="y")

# Enable mousewheel scrolling
def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", on_mousewheel)

# Content - all centered
tk.Label(frame,text="DNA Sequence Analyzer",font=("Segoe UI",24,"bold"),bg=BG,fg=ACC).pack(pady=20)

tk.Label(frame,text="Sequence 1:",font=("Segoe UI",12),bg=BG,fg=FG).pack(pady=(20,5))
seq1=scrolledtext.ScrolledText(frame,width=100,height=6,font=("Consolas",10))
seq1.pack(pady=5)

tk.Label(frame,text="Sequence 2:",font=("Segoe UI",12),bg=BG,fg=FG).pack(pady=(20,5))
seq2=scrolledtext.ScrolledText(frame,width=100,height=6,font=("Consolas",10))
seq2.pack(pady=5)

tk.Button(frame,text="Analyze DNA",bg=ACC,fg="black",font=("Segoe UI",14,"bold"),
          command=lambda: analyze(),padx=40,pady=10,cursor="hand2").pack(pady=30)

# Results section
results_frame=tk.Frame(frame,bg=BG)
results_frame.pack(pady=10,fill="x")

output=tk.Label(results_frame,bg=BG,fg=ACC,font=("Segoe UI",12),wraplength=900,justify="center")
output.pack(pady=10)

plot_frame=tk.Frame(frame,bg=BG)
plot_frame.pack(pady=20)

def analyze():
    for w in plot_frame.winfo_children(): w.destroy()

    s1=seq1.get("1.0","end").strip()
    s2=seq2.get("1.0","end").strip()

    if not s1 or not s2:
        output.config(text="Please enter both DNA sequences!")
        return

    kmp=len(kmp_search(s1,s2))
    sa=suffix_search(s1,s2,build_suffix_array(s1))
    mut=detect_mutations(s1,s2)
    score=needleman_wunsch(s1,s2)
    prob=predict_mutation_probability(len(mut))

    result_text = f"KMP Matches: {kmp} | Suffix Matches: {len(sa)} | Mutations: {len(mut)} | Alignment Score: {score} | Mutation Risk: {prob:.2f}"
    output.config(text=result_text)

    fig=plot_mutations(mut,len(s1))
    canvas_widget = FigureCanvasTkAgg(fig,plot_frame)
    canvas_widget.get_tk_widget().pack()
    
    # Update scroll region after adding plot
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
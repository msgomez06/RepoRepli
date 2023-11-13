# @title Required Imports and Verifications
import tkinter as tk
from tkinter import ttk
from IPython.display import display
import pandas as pd

questionnaire_path = (
    "/home/mgomezd1/repos/RepoRepli/Questionnaire/Questionnaire_Questions_master.xlsx"
)

# Load Spreadsheet data
df_fit = pd.read_excel(questionnaire_path, sheet_name="Fitting")
df_inf = pd.read_excel(questionnaire_path, sheet_name="Inference")


def create_questionnaire(df):
    # Create a tkinter window
    window = tk.Tk()
    window.title("Questionnaire")

    # Create a frame to hold the questions and answers
    frame = ttk.Frame(window, padding="10")
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Add a label for the question
    question_label = ttk.Label(
        frame, text=df["Question"][0], wraplength=500, justify="left"
    )
    question_label.grid(column=0, row=0, columnspan=2, pady=10)

    # Add radio buttons for each answer
    answer_options = [
        "Fully_Equivalent",
        "Approximately_Equivalent",
        "Somewhat_Equivalent",
        "Not_Equivalent_or_Applicable",
    ]
    selected_answer = tk.StringVar()
    radio_buttons = []

    for i, option in enumerate(answer_options):
        radio_button = ttk.Radiobutton(
            frame, text=option, variable=selected_answer, value=option
        )
        radio_button.grid(column=0, row=i + 1, sticky=tk.W)
        radio_buttons.append(radio_button)

    # Function to update the question and answers
    def update_question(index):
        print(index)
        question_label.config(text=df["Question"][index])
        for i, option in enumerate(answer_options):
            print(df[option][index])
            print(len(radio_buttons))
            radio_buttons[i].config(text=df[option][index])

    # Function to handle the "Next" button click
    def next_question():
        nonlocal current_question_index
        current_question_index += 1

        if current_question_index < len(df):
            update_question(current_question_index)
        else:
            window.destroy()

    # Add a "Next" button
    next_button = ttk.Button(frame, text="Next", command=next_question)
    next_button.grid(column=1, row=len(answer_options) + 1, pady=10)

    # Initialize the question and answers
    current_question_index = 0

    # Update the initial question and answers
    update_question(current_question_index)

    # Start the tkinter main loop
    window.mainloop()


create_questionnaire(df_fit)

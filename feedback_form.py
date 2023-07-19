import tkinter as tk

def submit_feedback():
    name = name_entry.get()
    email = email_entry.get()
    feedback_type = feedback_type_var.get()
    comments = comments_text.get(1.0, tk.END)

    print("Feedback Form Submitted!")
    print("Name:", name)
    print("Email:", email)
    print("Feedback Type:", feedback_type)
    print("Comments:")
    print(comments)

    # You can perform further processing or save the data to a file/database here.

    # Clear the form fields after submission.
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    feedback_type_var.set("General")
    comments_text.delete(1.0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("Feedback Form")

# Create form elements
tk.Label(app, text="Name:").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1)

tk.Label(app, text="Email:").grid(row=1, column=0, sticky="e")
email_entry = tk.Entry(app)
email_entry.grid(row=1, column=1)

tk.Label(app, text="Feedback Type:").grid(row=2, column=0, sticky="e")
feedback_types = ["General", "Bug Report", "Feature Request", "Other"]
feedback_type_var = tk.StringVar(app)
feedback_type_var.set("General")
feedback_type_menu = tk.OptionMenu(app, feedback_type_var, *feedback_types)
feedback_type_menu.grid(row=2, column=1)

tk.Label(app, text="Comments:").grid(row=3, column=0, sticky="e")
comments_text = tk.Text(app, width=30, height=10)
comments_text.grid(row=3, column=1)

submit_button = tk.Button(app, text="Submit", command=submit_feedback)
submit_button.grid(row=4, columnspan=2)

# Start the main event loop
app.mainloop()

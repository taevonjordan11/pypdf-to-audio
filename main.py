import pyttsx3
import PyPDF2
import tkinter as tk
# from tkinter.filedialog import askopenfilename
from tkinter import filedialog, messagebox

# Function to process the PDF and read it aloud
def read_pdf():
    # Open file dialog to select a PDF file
    pdf_path = filedialog.askopenfilename(title="Select a PDF File", filetypes=[("PDF Files", "*.pdf")])
    if not pdf_path:
        return  # Exit if no file is selected

    try:
        # Read the PDF file
        pdfreader = PyPDF2.PdfReader(pdf_path)
        pages = len(pdfreader.pages)

        # Initialize the text-to-speech engine
        player = pyttsx3.init()

        # Set speech rate
        rate = rate_slider.get()
        player.setProperty('rate', rate)

        # Extract text from each page and speak it
        for i in range(pages):
            page = pdfreader.pages[i]
            text = page.extract_text()
            if text.strip():
                player.say(text)

        player.runAndWait()
        messagebox.showinfo("Success", "Finished reading the PDF!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main application window
app = tk.Tk()
app.title("PDF to Audio Tool")
app.geometry("400x300")

# Add a label
label = tk.Label(app, text="PDF to Audio Tool", font=("Helvetica", 16))
label.pack(pady=10)

# Add a button to select and read the PDF
read_button = tk.Button(app, text="Select and Read PDF", command=read_pdf, font=("Helvetica", 12))
read_button.pack(pady=20)

# Add a slider to adjust the speech rate
rate_label = tk.Label(app, text="Adjust Speech Rate:", font=("Helvetica", 12))
rate_label.pack(pady=5)

rate_slider = tk.Scale(app, from_=50, to=300, orient="horizontal", length=300, font=("Helvetica", 10))
rate_slider.set(150)  # Default speech rate
rate_slider.pack(pady=10)

# Run the main event loop
app.mainloop()
import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Open a PDF file using a file dialog
pdf = askopenfilename(title="Select a PDF File", filetypes=[("PDF Files", "*.pdf")])

if pdf:  # Check if a file was selected
    pdfreader = PyPDF2.PdfReader(pdf)
    pages = len(pdfreader.pages)

    # Initialize the text-to-speech engine
    player = pyttsx3.init()

    rate = player.getProperty('rate')
    

    # Settings
    player.setProperty('rate', 175)
    print(f"current speech rate: {rate}")

    for i in range(pages):
        page = pdfreader.pages[i]
        text = page.extract_text()
        if text.strip():  # Check if the page contains any text
            player.say(text)

    # Run the text-to-speech engine
    player.runAndWait()
else:
    print("No file selected.")
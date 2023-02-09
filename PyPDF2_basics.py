#import the PyPDF2 module
from PyPDF2 import PdfReader
import os

#open the PDF file
reader = PdfReader("file.pdf")

# printing number of pages in pdf file
print(len(reader.pages))

num_pages = len(reader.pages)
 
# getting a specific page from the pdf file
page = reader.pages[0]

# getting all pages from the pdf file
all_pages_text = ""
for i in range(0, num_pages):
    all_pages_text += reader.pages[i].extract_text()

# extracting text from one page
text = page.extract_text()
print(text)

# extracting text from all pages
print(all_pages_text)

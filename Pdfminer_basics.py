from pdfminer.high_level import extract_text

text  = extract_text("/home/user/Desktop/file.pdf", 'rb')
print(text)

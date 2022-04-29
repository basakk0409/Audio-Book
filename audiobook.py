from matplotlib.pyplot import text
import pyttsx3 # module to convert text to speech
import PyPDF2 # text to read pdf
book = open('oop.pdf' , 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
n = int(input("Enter the page no. from which we have to read:- "))
for num in range(n-1, pages):
    page = pdfReader.getPage(n-1)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait() 



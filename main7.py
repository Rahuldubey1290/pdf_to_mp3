import PyPDF2
from gtts import gTTS


def main():
    def Text_to_speech():
        myAudio = gTTS(text=textString, lang='hi', slow=False)
        f_Name = input('Enter The File Name For Which You Want To Save\n')
        myAudio.save(f"{f_Name}.mp3")

    try:
        pdf_File = open('Presentation1.pdf', 'rb')
        pdf_Reader = PyPDF2.PdfFileReader(pdf_File, strict=False)
        count = pdf_Reader.numPages
        textList = []
        print(f"The total number of pages is :{count}")
        inp = int(input('Press 1 for single page and 2 for pages and 3 for all pages\n'))

        if inp == 1:
            page = int(input('Enter the page you want to read:\n'))
            pages = pdf_Reader.getPage(page)
            textString = (pages.extractText())
            print(textString)
            Text_to_speech()


        elif inp == 2:

            givenPage1 = int(input('Enter the starting page number:\n'))
            givenPage2 = int(input('Enter the finishing page number:\n'))
            for page in range(givenPage1, givenPage2 + 1):
                pages = pdf_Reader.getPage(page)
                textList.append(pages.extractText())
            textString = " ".join(textList)
            print(textString)
            Text_to_speech()

        elif inp == 3:
            for page in range(count):
                pages = pdf_Reader.getPage(page)
                textList.append(pages.extractText())
            textString = " ".join(textList)
            print(textString)
            Text_to_speech()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

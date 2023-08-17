import PyPDF2
import glob
from natsort import natsorted

pdf_writer = PyPDF2.PdfFileWriter()
# 選択されたPDFをすべて結合する
num=int(input("何分割しますか"))
for pdf_file in natsorted(glob.glob('./print/*.pdf')):
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    print(pdf_file)
    for i in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(i))
    j=0
    while True:
        if (pdf_reader.getNumPages()+j)%num==0:
            break
        else:
            p = pdf_reader.getPage(0)
            p_size = p.mediaBox
            p_width = p_size.getWidth()
            p_height = p_size.getHeight()
            pdf_writer.add_blank_page(width= p_width,height= p_height)
            print("いれたよ")
            j+=1


pdf_name = "yushow.pdf"
# 保存
with open(pdf_name, "wb") as f:
    pdf_writer.write(f)

print("終わり")
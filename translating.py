from reportlab.pdfbase import pdfmetrics, ttfonts
from googletrans import Translator
from googleOnlineTranslate import google_translate
import aspose.words as aw
import utils

src_path = 'source_data/'
tar_path = 'result_data/'

# 注册字体
pdfmetrics.registerFont(ttfonts.TTFont('yahei', 'C:\Windows\Fonts\msyh.ttc'))

# 使用Google Translate API来实现英文到中文的翻译，需要注册API key
# def google_translate(english_text):
#     translator = Translator()
#     chinese_text = translator.translate(english_text, src='en', dest='zh-cn').text
#     print(chinese_text)
#     return chinese_text


if __name__ == '__main__':
    paths = utils.get_file_names(src_path)
    for path in paths:
        p = path.split('.')
        en_txt = utils.file_read(src_path+path)
        cn_txt = google_translate(en_txt)
        print(cn_txt)
        txt_file = tar_path+p[0]+"_translated.txt"
        utils.file_write(txt_file, en_txt+"\n\n"+cn_txt)
        doc = aw.Document(txt_file)
        # 将 TXT 保存为 PDF 文件
        pdf_file = tar_path+p[0]+"_translated.pdf"
        doc.save(pdf_file, aw.SaveFormat.PDF)
        print(f"PDF文件已生成：{pdf_file}")



import fitz
import os


class PdfFile:
    def pdf_to_dict(self, pdf_file):
        pdf_file = os.path.join('.', 'source', f'{pdf_file}.pdf')
        doc = fitz.open(pdf_file)

        for current_page in range(len(doc)):
            page = doc.load_page(current_page)
            page_text = page.get_text("text")
            page_text_list = page_text.split('\n')
            page_text_dict = dict()

            for i in page_text_list:
                if ':' in i:
                    key, value = i.split(":", 1)
                    page_text_dict[key.strip()] = value.strip()
            return page_text_dict

import os
import PyPDF2

def extract_text_from_first_page(pdf_path, output_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        first_page = reader.pages[0]  # Extraer la primera página
        text = first_page.extract_text()

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(text)

# Directorio que contiene los archivos PDF
pdf_directory = 'C:/Users/luis.murcia/OneDrive - Autonal SAS/Escritorio/extraer pdf/pdf'

# Directorio donde se guardarán los archivos de texto extraídos
output_directory = 'C:/Users/luis.murcia/OneDrive - Autonal SAS/Escritorio/extraer pdf/texto'

# Iterar sobre todos los archivos PDF en el directorio
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        output_filename = os.path.splitext(filename)[0] + '_primerapagina.txt'
        output_path = os.path.join(output_directory, output_filename)
        extract_text_from_first_page(pdf_path, output_path)

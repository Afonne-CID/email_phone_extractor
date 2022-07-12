import os
import re
import PyPDF2
    

def pdf_extractor():

    email_regex = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
    phone_regex = re.compile (r'([-\.\s]??\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    
    pdf_files = list_of_files()
    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as pdf_obj:
            pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
            
            pdf_obj = ''
            count = pdf_reader.numPages
            for i in range(count):
                pdf_obj += str(pdf_reader.getPage(i).extractText())
                
            phone = str(phone_regex.findall(pdf_obj)).replace('[', '').replace(']', '')
            email = str(email_regex.findall(pdf_obj)).replace('[', '').replace(']', '')

            with open('extracted_contacts', 'a') as extracts:
                extracts.write('{}, {}\n'.format(phone if len(phone) > 0 else '', email if len(email) > 0 else ''))
    
    print('Action was successful')
    return 


def list_of_files():
    pdf_files = []
    path_of_the_directory= 'C:/Users/CID/Desktop/pdf_files'
    for filename in os.listdir(path_of_the_directory):
        f = os.path.join(path_of_the_directory, filename)
        if os.path.isfile(f):
            pdf_files.append(f)

    return pdf_files

pdf_extractor()
# print(pdf_extractor('C:/Users/CID/Documents/cid/cid_resume.pdf'))
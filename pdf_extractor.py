import os
import re
import PyPDF2
import requests


def pdf_extractor():

    # email_regex = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+[a-zA-Z]')
    email_regex = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]{3}')
    phone_regex = re.compile (r'([-\.\s]??\d{3}[-\.\s]??\d{3}[-\.\s]??\d{5}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{5}|\d{3}[-\.\s]??\d{5})')
    
    pdf_files = list_of_files()
    keys = pdf_files.keys()

    for key in keys:
        print(key + '...')
        for pdf_file in pdf_files[key]:
            with open(pdf_file, 'rb') as pdf_obj:
                pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
                
                pdf_obj = ''
                count = pdf_reader.numPages
                for i in range(count):
                    pdf_obj += str(pdf_reader.getPage(i).extractText())
                    
                phone = str(phone_regex.findall(pdf_obj))\
                        .replace('[', '').replace(']', '')\
                        .replace(' ', '')\
                        .strip("'")\
                        .replace(',', ' ')\

                email = str(email_regex.findall(pdf_obj))\
                        .replace('[', '')\
                        .replace(']', '')\
                        .strip("'")

                with open(key + '.txt', 'a+', encoding="utf-8") as extracts:
                    details = '{}, {}\n'.format(phone.strip("'") if len(phone) > 0 else '', email if len(email) > 0 else '')
                    contact = details.strip("'")
                    extracts.write(contact.strip("'"))
        
    print('Action was successful')
    return


def list_of_files():

    pdf_files = {}
    path_of_the_directory= 'C:/Users/CID/Desktop/pdf_files/'
    for state_name in os.listdir(path_of_the_directory):
        state = []
        for file_name in os.listdir(path_of_the_directory + state_name):
            f = os.path.join(path_of_the_directory, state_name + '/' + file_name)
            if os.path.isfile(f):
                state.append(f)
        pdf_files[state_name] = state

    return pdf_files

pdf_extractor()



import re


def phone_extractor(text_file=''):
     
     with open('saved_filed.txt', 'r') as file:
            text_file = str(file.readlines())

            # text_file = '\n\nAFONNE\n-\nCID PAUL ONYEDIKACHI\n \n\n  \n(+234)8071231219\n  \n \n|\n  \ndelightinbusiness@gmail.com'
            phone_regex = re.compile (r'([-\.\s]??\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
            phone = phone_regex.findall(text_file)
            
            print(phone if phone else 'not found')

phone_extractor()
import search_functions
import os
import shutil
import sys

chem_eng_path = '/Users/cairo/Chem Eng/' # the pathway in which the school files will be sorted into
downloads_path = '/Users/cairo/Downloads/' # downloads folder in which files will be sorted out of
financial_path = '/Users/cairo/Financial/' # the pathway in which financial documents will be moved to
taxes_path = '/Users/cairo/Financial/Taxes' # path where tax related files shall be moved into
other_path = '/Users/cairo/Other/' # folder in which rnadom images will be moved to


downloads_folder = os.listdir(downloads_path)
chem_eng_folder = os.listdir(chem_eng_path)

course_code_list = ['APS', 'CHE', 'MAT', 'JRE', 'CIV', 'MIE', 'CSC', 'ECE', 'PEY']
important_key_words = ['Contract', 'Banking', 'Invoice', 'RESP', 'Pay']
taxes_key_words = ['Taxes', 'TFSA','T4', 'T2202']

for file in downloads_folder:  # loops through each file in downloads folder
    # Sorting School Related Flies - Operates under the assumptions that files will be named with course codes of the format AAA### only occuring once in the name
    for code in course_code_list:  # loops through the course code prefixes
        if code in file:  # checks if the course code prefix is in the file name
            start = file.index(code)  # retrieve course code
            if code != 'PEY': # PEY is coop programming, does not have numbers after code
                course_code = file[start: start + 6] # All course codes are of the format 'CHE###' 
                if course_code[3:-1].isnumeric() != True: # checks that the cource code is valid
                    sys.exit(f"Error: The file \"{file}\" has an invalid course code \"{course_code}\".")
            else:
                course_code = 'PEY'

            # Goes through each file possible contained in starting directory and checks for folder contianing the course code in the name
            new_location = search_functions.folder_search(course_code, chem_eng_path)
            if new_location is None:
                sys.exit(f"Error: There is no directory with course code \"{course_code}\" for the file \"{file}\".")

            # Moves file to the found directory
            shutil.move(os.path.join(downloads_path, file), new_location)

    # Sorting Important Files
    for word in important_key_words:  # loops through each key word and sees if its in the file name
        if word.lower() in file.lower():
            financial_location = search_functions.folder_search(word, financial_path)
            if financial_location is not None:
                shutil.move(os.path.join(downloads_path, file), financial_location)
            else:
                shutil.move(os.path.join(downloads_path, file), financial_path)
    for word in taxes_key_words:
        if word.lower() in file.lower():
            shutil.move(os.path.join(downloads_path, file), taxes_path)

    # Sorting Images
    if 'png' in file or 'jpg' in file or 'jpeg' in file or 'webp' in file or 'mov' in file or 'mp4' in file or 'mp3' in file:
        shutil.move(os.path.join(downloads_path, file), other_path)
print('Files Sorted Successfully!')
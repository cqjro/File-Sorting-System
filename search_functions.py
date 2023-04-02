import os


def folder_search(string, directory):
    """
    (str, str) -> str or None
    Searches through all files contained within the specified directory for a folder with a specified string
    """
    # ensure that the directory string can be concatenated with other files

    folder_files = os.listdir(directory)  # creates list of the folders files
    for item in folder_files:  # loops through each file in the folder
        item_path = os.path.join(directory, item) # creates path for the item in the directory
        if os.path.isdir(item_path) and string in item:  # checks if the file is a folder and contains the code
            return item_path  # returns the directory of the folder containing the course code
        elif os.path.isdir(item_path):
            search = folder_search(string, item_path)  # searches the item if it's a folder
            if search is not None:  # if it finds something, returns the result to main
                return search
    return None


def file_search(string, directory):
    """
    (str, str) -> str or None
    Searches through all files contained within the specified directory for a file with a specified name (string)
    """
    folder_files = os.listdir(directory)  # creates a list of the items in folder
    for item in folder_files:  # loops through each file in the folder
        item_path = os.path.join(directory, item) # creates path for the item in the directory
        if item == string: # returns the item path if the item is what is being looked for
            return item_path
        elif os.path.isdir(item_path): # searches through the item if it is a directory
            search = file_search(string, item_path)
            if search is not None:
                return search
    return None


def folder_duplicate_search(directory):
    """
    (str) -> dictionary
    Searches through a specified directory and returns a dictionary containing the titles of files as keys
    and the number of times the file occurs as values
    """
    item_dictionary = dict()  # accumulates the items and number of occurrences

    folder_files = os.listdir(directory)  # creates list of files in folder
    for item in folder_files:  # loops through each file in the folder
        item_path = os.path.join(directory, item)  # path of the current item
        if os.path.isdir(item_path):  # checks if the current item is a folder
            for key, values in folder_duplicate_search(item_path).items():  # iterates dup search results if folder
                if key in item_dictionary.keys():  # if key is in item dictionary, increases count
                    item_dictionary[key] += 1
                else:  # if key is not present in dictionary, sets count to 1
                    item_dictionary[key] = 1
        else:  # if item in folder isn't a folder, updates number of occurrences
            if item in item_dictionary.keys():
                item_dictionary[item] += 1
            else:
                item_dictionary[item] = 1
    return item_dictionary


def list_similarity(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3

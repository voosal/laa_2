'''Lab 2.2'''
import json

def read_the_file():
    '''
    Returns a dictinary of a read file
    '''
    print("-------------------------------------")
    while True:
        file_name = input('Enter the file name >>> ')
        print("-------------------------------------")
        try:
            with open(file_name, encoding='utf-8') as file:
                data = json.load(file)
            return data
        except:
            print("-------------------------------------")
            print("The file doesn't exist(")
            print("-------------------------------------")

def scan_main_file(data):
    '''
    Gives the user an opportunity to go over a dictionary
    '''
    if isinstance(data, dict):
        print("-------------------------------------")
        print("The item is a dictionary that has ", len(data), " elements")
        print("-------------------------------------")
        print("Here are all the keys:")
        for key in data:
            print("Key: " + str(key))
        while True:
            keyy = input("Please, select the key: >>> ")
            if keyy not in data:
                print("You didn't enter a key from a dictinary")
            else:
                break

        scan_main_file(data[keyy])

    elif isinstance(data, list):
        print("-------------------------------------")
        print("The item is a list that has ", len(data), " elements")
        print("-------------------------------------")
        print("Here are the items: ")
        i = 1
        for element in data:
            print(str(i) + ". " + str(element))
            i += 1
        print("")
        while True:
            index = input("Select the element: >>> ")
            if index.isdigit():
                index = int(index)
                if index > 0 and index <= len(data):
                    break
            print("Entered index doesn't exist")

        scan_main_file(data[index-1])

    else:
        print("-------------------------------------")
        print("The result is: ", str(data))
        print("-------------------------------------")

def main():
    data = read_the_file()
    scan_main_file(data)

main()

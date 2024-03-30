# import openpyxl

def read_txt(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        split_text = text.split('\n')
        for entry in split_text:
            people = entry.split('】')
            for person in people:
                if len(person) > 0:
                    data.append(person.strip())
    return data


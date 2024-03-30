# import openpyxl

def read_txt(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        split_text = text.split('】')
        for entry in split_text:
            if len(entry) > 0:
                data.append(entry)
    return data


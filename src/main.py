import os
# import time
import pandas as pd
# import requests
# import datetime
# import openai 
# import openpyxl
from utils.text_manip import *
from utils.api.to_gpt import *
def main():
    file_path = "data/rwdata_simple.txt"
    data = read_txt(file_path)
    formated_data = toGPT(data)

if __name__ == "__main__":
    main()
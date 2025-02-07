import numpy as np


class Data:

    @staticmethod
    def read_to_array():
        # Read a list of numbers from user and put into an array
        data_str = input("Enter Data: ")
        data_list = data_str.split(";")  # split string into list of strings
        data_array = np.array(data_list, dtype=int)  # convert to numpy array
        return data_array

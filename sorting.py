from data import Data


class Sort:

    @staticmethod
    def sort_data():
        my_array = Data.read_to_array()
        my_array.sort()
        return my_array

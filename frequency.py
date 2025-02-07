
class Frequency:

    @staticmethod
    def find_frequency(data_array):
        range_min = float(input("Min bound: "))
        range_max = float(input("Max bound: "))
        freq = 0
        for i in data_array:
            if range_min <= i <= range_max:
                freq += 1

        return freq

from sorting import Sort
from frequency import Frequency


def main():
    # Gather data in an array
    sorted_array = Sort.sort_data()
    print(sorted_array)

    freq = Frequency.find_frequency(sorted_array)
    print(freq)


if __name__ == "__main__":
    main()

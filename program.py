import csv
import os
from data_types import Purchase

#comment here 1
def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('---------------------------')
    print('Real Estate Data Mining App')
    print('---------------------------')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            print(type(row), row)
            print("Bed Count: {}, type: {}".format(row['beds'], type(row['beds'])))
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        # header = fin.readline().strip()
        # reader = csv.reader(fin, delimiter=",")
        # for row in reader:
        #     print(type(row), row)
        #     beds = row[4]


# def load_file_basic(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('found header: ' + header)
#
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             bed_count = line_data[4]
#             lines.append(line_data)
#
#         print(lines[:5])


def query_data(data):
    pass


if __name__ == '__main__':
    main()
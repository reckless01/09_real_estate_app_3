import csv
import os
from data_types import Purchase


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
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        # print(purchases[0].__dict__)
        return purchases

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
    # most/lease expensive house
    # average price house
    # average price 2 bedroom house

    # most expensive
    high_purchase = data[-1]
    print("The most expensive house is ${:,}, with {} beds and {} baths".format(
        high_purchase.price, high_purchase.beds, high_purchase.baths))

    # least expensive
    low_purchase = data[0]
    print("The least expensive house is ${:,}, with {} beds and {} baths".format(
        low_purchase.price, low_purchase.beds, low_purchase.baths))

    # sorted by price
    data.sort(key=lambda p: p.price)
    pass


if __name__ == '__main__':
    main()
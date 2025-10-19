import csv
from Customer import Customer


def import_customers(csvfile) -> list[Customer]:
    customer_list: list[Customer] = []
    for cl in csv.reader(csvfile):
        customer_list.append(
            Customer(cl[0], cl[1], cl[2], cl[3], cl[4], cl[5], cl[6], cl[7], cl[8])
        )
    return customer_list


def main():
    print()


if __name__ == "__main__":
    main()

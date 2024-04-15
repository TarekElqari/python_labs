from prettytable import PrettyTable
import random

def generate_fake_data(attributes, num_rows):
    data = []
    for _ in range(num_rows):
        row = [random.randint(1, 100) for _ in range(len(attributes))]
        data.append(row)
    return data

def create_table(table_name, attributes, num_rows):
    table = PrettyTable()
    table.field_names = attributes
    fake_data = generate_fake_data(attributes, num_rows)
    for row in fake_data:
        table.add_row(row)
    return table

def main():
    table_name = input("Enter the name of the table: ")
    attributes = input("Enter the attributes separated by comma: ").split(',')
    num_rows = int(input("Enter the number of rows: "))

    table = create_table(table_name, attributes, num_rows)
    print(table)

if __name__ == "__main__":
    main()

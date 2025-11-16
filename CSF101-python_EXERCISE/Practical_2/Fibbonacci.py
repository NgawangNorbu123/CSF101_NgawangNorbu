import csv

def read_csv_file(filename):
    with open(filename, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(', '.join(row))

# First, create a sample CSV file
with open('sample.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerow(['Alice', '30', 'New York'])
    csv_writer.writerow(['Bob', '25', 'Los Angeles'])

print("Contents of sample.csv:")
read_csv_file('sample.csv')

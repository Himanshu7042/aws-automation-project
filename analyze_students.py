import csv

threshold = 80  # You can change this

with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    print(f"Students with grade above {threshold}:")

    for row in reader:
        if int(row['grade']) > threshold:
            print(f"- {row['name']} ({row['grade']})")
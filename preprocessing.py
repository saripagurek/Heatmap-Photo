import csv


def reformat(given_csv, room_length, img_length):
    list_x = []
    list_z = []
    scale = img_length / room_length

    with open(given_csv, newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        num_rows = len(reader)
        for r in range(1, num_rows):
            row = reader[r]
            if len(row) == 2:
                x = float(row[0])
                z = float(row[1])
                list_x.append(x)
                list_z.append(z)

    with open('temp.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(list_x)):
            cur_x = int(list_x[i])
            cur_z = int(list_z[i])

            cur_x = cur_x + (0.5 * room_length)
            cur_z = cur_z + (0.5 * room_length)
            new_x = int(cur_x * scale)
            new_z = int(cur_z * scale)

            if new_x > (0.5 * img_length):
                new_x = new_x - 100
            elif new_x < (0.5 * img_length):
                new_x = new_x + 100
            if new_z > (0.5 * img_length):
                new_z = new_z - 100
            elif new_z < (0.5 * img_length):
                new_z = new_z + 100
            
            row = [new_x, new_z]
            writer.writerow(row)

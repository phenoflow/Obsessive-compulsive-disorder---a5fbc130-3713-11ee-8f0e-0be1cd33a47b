# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"E203.00","system":"readv2"},{"code":"E203z00","system":"readv2"},{"code":"Eu42.00","system":"readv2"},{"code":"Eu42y00","system":"readv2"},{"code":"Eu42z00","system":"readv2"},{"code":"15566.0","system":"med"},{"code":"18399.0","system":"med"},{"code":"2030.0","system":"med"},{"code":"20634.0","system":"med"},{"code":"21836.0","system":"med"},{"code":"22019.0","system":"med"},{"code":"22721.0","system":"med"},{"code":"24251.0","system":"med"},{"code":"3208.0","system":"med"},{"code":"38809.0","system":"med"},{"code":"47365.0","system":"med"},{"code":"5304.0","system":"med"},{"code":"5678.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('obsessive-compulsive-disorder-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["obsessivecompulsive---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["obsessivecompulsive---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["obsessivecompulsive---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

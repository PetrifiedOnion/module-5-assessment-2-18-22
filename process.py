log_file = open("um-server-01.txt") 
# Line one is opening the "um-server-01.txt" allowing it contents to be pulled and used here in this process.py file.


def sales_reports(log_file):
    # ^ The function of sale_reports is defined with log_file, the variable from above being utilized as the element.
    for line in log_file:
        # ^ a for loop is being made in which 
        line = line.rstrip()
        day = line[0:3]
        if day == "Tue":
            print(line)


sales_reports(log_file)

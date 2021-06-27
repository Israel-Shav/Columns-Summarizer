import sys, os, logging, csv

def usage():
    # Usage of sum-columns
    return "\nusage:\n\t$ python3 sum-columns.py <filename> <column-number>\n\nexample:\n\t$ python3 sum-columns.py expenses.csv 3\n"

def main():
    NUM_OF_ARGS = 2
    # Define logger and check argumnets format
    logger = logging.getLogger("Main")
    if len(sys.argv) != NUM_OF_ARGS + 1:
        logger.error(usage())
        exit(1)
    # VAlidate file name
    fileName = sys.argv[1]
    if not os.path.isfile(fileName):
        logger.error(f"{usage()}\nError: <filename> must be a file, check if is it exist!\n")
        exit(2)
    # Validate column index
    columnIndex = sys.argv[2]
    if not columnIndex.isdigit() or int(columnIndex) <= 0 :
        logger.error(f"{usage()}\nError: <column-number> must be integer greater than 0!\n")
        exit(3)
    # Index starts from 0
    columnIndex = int(columnIndex) - 1
    with open(fileName) as csvfile:
        # GEt iterable object
        spamreader = csv.reader(csvfile, delimiter=',')
        # Get rid of the columns line and check array bounds
        if len(next(spamreader)) < columnIndex + 1:
            logger.error(f"{usage()}\nError: <column-number> is out of index!\n")
            exit(4)
        sum = 0
        # Integers flag
        isInt = True
        for row in spamreader:
            _sum = row[columnIndex]
            try:
                _sum = float(_sum)
                if isInt and not _sum.is_integer():
                    isInt = False
            except ValueError:
                print(row[columnIndex])
                logger.error("\nThe selected column is a text column, plese select other <column-number>!\n")
                exit(5)
            sum += _sum
        sum = int(sum) if isInt else round(sum, 2)
        print(f"The total 'amount' is {sum}")
    

main()
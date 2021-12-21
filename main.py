import pandas
import sys
import os
import pyarrow
import logging

logging.basicConfig(filename="PRQ_CSV.log", level=logging.INFO)
str_path = sys.argv[1]
try:
    str_save = sys.argv[2]
except Exception:
    print("no save Path")
print(str_path)
logging.info("Path read")
try:
    file = pandas.read_parquet(str_path)

except Exception as err:
    logging.error(err)
    exit()

try:
    file.to_csv(str_save)
    logging.info("Process finished")
except Exception as err:
    try:
        file.to_csv()
        logging.info("Due to invalid Path, the file was saved to standard Path")
    except Exception:
        logging.critical(err)
        logging.critical("File was not saved")


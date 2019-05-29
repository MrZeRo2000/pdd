
import logging
import os
import cx_Oracle

LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s %(module)s %(message)s"
CONNECTION_STRING = "drivenow_bi/drivenow_bi@10.100.38.84:1521/sxbista_rw.sixt.de"

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger = logging.getLogger("PDD")

logger.setLevel(logging.INFO)
logger.addHandler(console_handler)

try:
    logger.info("Started")

    connection = cx_Oracle.connect(CONNECTION_STRING)
    logger.info("Connected to database")

    cursor = connection.cursor()

    try:
        result = cursor.execute("SELECT COUNT(*) FROM dual")
        rows = result.fetchmany(1)

        logger.info("Test query returned value: " + str(rows[0][0]))
    finally:
        cursor.close()

    logger.info("Finished")
except Exception as e:
    logger.fatal(e, exc_info=True)
    exit(1)


import logging
import os
import cx_Oracle

LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s %(module)s %(message)s"

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger = logging.getLogger("PDD")

logger.setLevel(logging.INFO)
logger.addHandler(console_handler)

try:
    logger.info("Started")

    connection_string = os.environ["CONNECTION_STRING"]
    logger.info("Obtained connection string:" + connection_string)

    connection = cx_Oracle.connect(connection_string)
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

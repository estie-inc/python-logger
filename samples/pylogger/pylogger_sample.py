import sys

sys.path.append("../../")

from pylogger import pylogger


def get_logger_sample():
    logger = pylogger.get_logger(name="test")

    logger.debug("DEBUG TEST")
    logger.info("INFO TEST")
    logger.warning("WARNING TEST")
    logger.error("ERROR TEST")
    logger.critical("CRITICAL TEST")


def get_default_logger_sample():
    logger = pylogger.get_default_logger()

    logger.debug("DEBUG TEST")
    logger.info("INFO TEST")
    logger.warning("WARNING TEST")
    logger.error("ERROR TEST")
    logger.critical("CRITICAL TEST")


def get_class_default_logger_sample():
    logger = pylogger.get_class_default_logger(class_name="TestClass")

    logger.debug("DEBUG TEST")
    logger.info("INFO TEST")
    logger.warning("WARNING TEST")
    logger.error("ERROR TEST")
    logger.critical("CRITICAL TEST")


def json_logger_sample():
    json_items = {"test": "test"}

    pylogger.json_logger_debug(json_items=json_items, msg="DEBUG TEST")
    pylogger.json_logger_info(json_items=json_items, msg="DEBUG TEST")
    pylogger.json_logger_warning(json_items=json_items, msg="WARNING TEST")
    pylogger.json_logger_error(json_items=json_items, msg="ERROR TEST")
    pylogger.json_logger_critical(json_items=json_items, msg="CRITICAL TEST")


def main():
    logger = pylogger.get_default_logger()

    logger.info("Try using get_logger")
    get_logger_sample()

    logger.info("Try using get_default_logger")
    get_default_logger_sample()

    logger.info("Try using get_class_default_logger")
    get_class_default_logger_sample()

    logger.info("Try using json_logger")
    json_logger_sample()


if __name__ == "__main__":
    sys.exit(main())

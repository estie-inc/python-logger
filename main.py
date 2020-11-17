# -*- coding: utf-8 -*-

import logging

logging.basicConfig(
    format='%(asctime)s [%(levelname)s:%(lineno)s] [%(name)s] %(message)s',
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def main():
    LOGGER.info('Hello! こんにちは! 123')
    LOGGER.info('これは main.py での出力の例です')


if __name__ == '__main__':
    main()

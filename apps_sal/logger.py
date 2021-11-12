import logging as _logging


_logger = None


def get_logger() -> _logging.Logger:
    global _logger
    if not _logger:
        _logger = _logging.getLogger('apps-sal')
        if not _logging.getLogger().handlers:
            formatter = _logging.Formatter(fmt='%(asctime)s apps-sal [%(levelname)s] %(message)s',
                                           datefmt='%Y-%m-%d %H:%M:%S')
            stderr_handler = _logging.StreamHandler()
            stderr_handler.setFormatter(formatter)
            _logger.addHandler(stderr_handler)
    return _logger

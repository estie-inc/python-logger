import datetime
import inspect
import json
import logging
from typing import Callable

_JSON_INDENT = 4
_JSON_SEPERATORS = (",", ": ")

_DEPTH_RECURSION_DEFAULT = 1
_DEPTH_RECURSION_GET_LOGGER = 2
_DEPTH_RECURSION_JSON_LOGGER = 3

_LOGGING_LEVEL = logging.INFO if not __debug__ else logging.DEBUG
_FORMATTER_STR_DETAILED = (
    "%(asctime)s (PID:%(process)d) %(levelname)s %(name)s %(message)s"
)
_FORMATTER_STR = _FORMATTER_STR_DETAILED


def get_method_name(
    module_name: str = None,
    class_name: str = None,
    depth_recursion: int = _DEPTH_RECURSION_DEFAULT,
):
    """Retrieves a method name with a module name and class name.

    :param module_name: Module name
    :type module_name: str

    :param class_name: Class name
    :type class_name: str

    :param depth_recursion: Depth of recursive call for call stacks (>=1)
    :type depth_recursion: int

    :return: Method name
    :rtype: str
    """
    if depth_recursion < 1:
        raise ValueError(f"depth_recursion is not natural number. - {depth_recursion}")

    name = None

    f_stack = inspect.currentframe()
    for _ in range(depth_recursion):
        f_stack = f_stack.f_back

    if f_stack is None:
        raise ValueError("Reached the call stack limit.")

    method_name = f_stack.f_code.co_name

    if module_name is None and class_name is None:
        name = method_name
    elif class_name is not None:
        name = f"{class_name}.{method_name}"
    elif module_name is not None:
        name = f"{module_name}.{method_name}"
    else:
        name = f"{module_name}.{class_name}.{method_name}"
    return name


def _logging_base_decorator(func_logging_decorator: Callable):
    """Decorator Function with Parameters.

    :param func_logging_system: Function object for Decoration
    :type func_logging_system: Function object

    :return:  Wrapper function's object
    :rtype: Callable
    """

    def wrapper(*args, **kwargs):
        def wrapper_logging_decorator(func_get_logger):
            return func_logging_decorator(func_get_logger, *args, **kwargs)

        return wrapper_logging_decorator

    return wrapper


@_logging_base_decorator
def _logging_decorator(
    func_get_logger: Callable, level: int = _LOGGING_LEVEL, is_propagate: bool = False
):
    """Decorator Function for Python Logging.

    :param func_get_logger: Function object for Decoration
    :type func_get_logger: function

    :param level: Logging Level
    :type level: int

    :param is_propagate: Need Propagation or not (False: Not propagate / True: Propagate)
    :type is_propagate: bool

    :return Wrapper function's object
    :rtype: Callable
    """
    handler = logging.StreamHandler()

    handler.setLevel(level)

    formatter = logging.Formatter(_FORMATTER_STR)
    handler.setFormatter(formatter)

    def wrapper(name):
        logger = func_get_logger(name)
        if handler is not None:
            logger.addHandler(handler)
        logger.setLevel(level)
        logger.propagate = is_propagate
        return logger

    return wrapper


@_logging_decorator()
def get_logger(name: str):
    """Gets a logger with the name.

    :param name: Name of the logger
    :type name: str

    :return Logger
    :rtype: object
    """
    return logging.getLogger(name=name)


def get_default_logger():
    """Gets a logger with the method name.

    :return Logger
    :rtype: object
    """
    return get_logger(name=get_method_name(depth_recursion=_DEPTH_RECURSION_GET_LOGGER))


def get_class_default_logger(class_name: str, module_name: str = None):
    """Gets a logger with the class name.

    :param class_name: Class name.
    :type class_name: str

    :param class_name: (optional) Module name.
    :type class_name: str

    :return Logger
    :rtype: object
    """
    return get_logger(
        name=get_method_name(
            module_name=module_name,
            class_name=class_name,
            depth_recursion=_DEPTH_RECURSION_GET_LOGGER,
        )
    )


def _json_serialize(obj: object):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


def _json_dumps(json_items):
    return json.dumps(
        json_items,
        indent=_JSON_INDENT,
        ensure_ascii=False,
        sort_keys=True,
        separators=_JSON_SEPERATORS,
        default=_json_serialize,
    )


def json_logger(
    level,
    json_items,
    module_name=None,
    class_name=None,
    depth_recursion=2,
    msg=None,
):
    get_logger(
        get_method_name(
            module_name=module_name,
            class_name=class_name,
            depth_recursion=depth_recursion,
        )
    ).log(level=level, msg=msg)
    get_logger(
        get_method_name(
            module_name=module_name,
            class_name=class_name,
            depth_recursion=depth_recursion,
        )
    ).log(level=level, msg=_json_dumps(json_items))


def json_logger_debug(json_items, module_name=None, class_name=None, msg=None):
    json_logger(
        level=logging.DEBUG,
        json_items=json_items,
        module_name=module_name,
        class_name=class_name,
        depth_recursion=_DEPTH_RECURSION_JSON_LOGGER,
        msg=msg,
    )


def json_logger_info(json_items, module_name=None, class_name=None, msg=None):
    json_logger(
        level=logging.INFO,
        json_items=json_items,
        module_name=module_name,
        class_name=class_name,
        depth_recursion=_DEPTH_RECURSION_JSON_LOGGER,
        msg=msg,
    )


def json_logger_warning(json_items, module_name=None, class_name=None, msg=None):
    json_logger(
        level=logging.WARNING,
        json_items=json_items,
        module_name=module_name,
        class_name=class_name,
        depth_recursion=_DEPTH_RECURSION_JSON_LOGGER,
        msg=msg,
    )


def json_logger_error(json_items, module_name=None, class_name=None, msg=None):
    json_logger(
        level=logging.ERROR,
        json_items=json_items,
        module_name=module_name,
        class_name=class_name,
        depth_recursion=_DEPTH_RECURSION_JSON_LOGGER,
        msg=msg,
    )


def json_logger_critical(json_items, module_name=None, class_name=None, msg=None):
    json_logger(
        level=logging.CRITICAL,
        json_items=json_items,
        module_name=module_name,
        class_name=class_name,
        depth_recursion=_DEPTH_RECURSION_JSON_LOGGER,
        msg=msg,
    )

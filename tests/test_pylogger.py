import sys

import pytest

sys.path.append("../")

from pylogger import pylogger


@pytest.mark.parametrize(
    "module_name, class_name, expected",
    [
        (None, None, "test_get_method_name"),
        (None, "TestClass", "TestClass.test_get_method_name"),
        ("TestModule", None, "TestModule.test_get_method_name"),
        ("TestModule", "TestClass", "TestModule.TestClass.test_get_method_name"),
    ],
    ids=["both_none", "only_class", "only_module", "both"],
)
def test_get_method_name(module_name, class_name, expected):
    assert (
        pylogger.get_method_name(module_name=module_name, class_name=class_name)
        == expected
    )

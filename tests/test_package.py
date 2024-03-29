from typing import Dict

from util_common.package import get_package_info


def test_get_package_info():
    info = get_package_info('pip')
    assert isinstance(info, Dict)
    assert info.get('name') == 'pip'

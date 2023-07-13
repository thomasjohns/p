import pytest

from p import ArgumentKind
from p import parse_argument


@pytest.mark.parametrize(
    ('arg', 'expected_result'),
    [
        ('', None),
        ('kubectl get pods -n default', 'command'),
        ('ping other-server.edu', 'command'),
        ('server.edu', 'host'),
    ],
)
def test_parse_argument(arg: str, expected_result: ArgumentKind) -> None:
    assert parse_argument(arg) == expected_result

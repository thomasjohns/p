import sys
from typing import assert_never
from typing import Literal


VERSION = '0.1.0'


ArgumentKind = Literal['host', 'command'] | None


def parse_argument(arg: str) -> ArgumentKind:
    if arg:
        has_dot = '.' in arg
        is_one_token = ' ' not in arg
        if has_dot and is_one_token:
            return 'host'
        else:
            return 'command'
    else:
        return None


def main() -> int:
    p_argument = ' '.join(sys.argv[1:])
    argument_kind = parse_argument(p_argument)
    match argument_kind:
        case 'host':
            print(f'host: {p_argument}')
        case 'command':
            print(f'command: {p_argument}')
        case None:
            print('no argument')
        case _:  # pyright: ignore reportUnnecessaryComparison
            assert_never(argument_kind)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

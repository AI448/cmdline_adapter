from typing import TypeVar
from collections.abc import Callable
from argparse import ArgumentParser
from inspect import signature


T = TypeVar("T")


def generate_parser(callable: Callable) -> ArgumentParser:

    parser = ArgumentParser()
    for name, parameter in signature(callable).parameters.items():
        kwargs = {}
        if parameter.annotation != parameter.empty:
            kwargs["type"] = parameter.annotation
            kwargs["help"] = parameter.annotation.__name__
        if parameter.default != parameter.empty:
            kwargs["default"] = parameter.default
            kwargs["required"] = False
        else:
            kwargs["required"] = True
#        print(name, kwargs)
        parser.add_argument("--" + name, **kwargs)

    return parser


def call(callable: Callable[..., T]) -> T:
    parser = generate_parser(callable)
    args = parser.parse_args()
    return callable(**{name: getattr(args, name) for name in signature(callable).parameters.keys()})

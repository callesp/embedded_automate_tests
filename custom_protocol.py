import struct
from enum import Enum


class Cmd(Enum):
    Action1 = 0x01
    Action2 = 0x02
    Action3 = 0x03
    Action4 = 0x04
    Action5 = 0x05
    Action6 = 0x06
    Action7 = 0x07


class RequestFrame:
    parsing_schema = ''

    def __init__(self) -> None:
        self.cmd = 0
        self.data = None


class FeatureOneRequest:
    def __init__(self) -> None:
        pass


class FeatureTwoRequest:
    def __init__(self) -> None:
        pass


class FeatureThreeRequest:
    def __init__(self) -> None:
        pass


class ResponseFrame:
    parsing_schema = ''

    def __init__(self) -> None:
        pass


class FeatureOneResponse:
    def __init__(self) -> None:
        pass


class FeatureTwoResponse:
    def __init__(self) -> None:
        pass


print(Cmd.Action1.value)

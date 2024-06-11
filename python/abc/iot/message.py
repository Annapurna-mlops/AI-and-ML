from dataclasses import dataclass
from enum import Enum, auto

"""
The enum.auto() method is only available in Python 3.4 and later.
The enum.auto() method can be used with any type of enum, including IntEnum and Flag.
The enum.auto() method will always assign unique values to enum members.
The enum.auto() method can be used to generate values for enum members that are defined in a separate module.
Overall, the enum.auto() method is a convenient and powerful tool for generating values for enum members.
"""
class MessageType(Enum):
    SWITCH_ON = auto()
    SWITCH_OFF = auto()
    CHANGE_COLOR = auto()
    PLAY_SONG = auto()
    OPEN = auto()
    CLOSE = auto()

    """The @dataclass decorator examines the class to find field s.
    A field is defined as a class variable that has a type annotation.
    """

@dataclass
class Message:
    device_id: str
    msg_type: MessageType
    data: str = ""

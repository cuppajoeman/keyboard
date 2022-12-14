"""
Note:
In this situation a note is number which represents a certain offset
from a base frequency. For example if we set C3 to be our base note,
then D3 would be represented by 2. B4 would be -1, C#4 would be 12.

Anchor Note:
An Anchor note is a note which is considered the main note and what
other notes are compared against

Anchor Interval:
An anchor interval is defined in terms of an anchor note and a normal
note, it is the number of notes between the anchor note and the note.
If we set our anchor note to 8, then 11 has an anchor interval of 3.
If we set our anchor note to -3, then 3 has an anchor interval of 6.
If we set our anchor note to 24, then 57 has an anchor interval of 33.
"""
from typing import List

from operation import keyboard
import constants

INTERVAL_TO_COMPLEXITY = {
    0: 0,
    1: 10,
    2: 4,
    3: 7,
    4: 2,
    5: 5,
    6: 9,
    7: 1,
    8: 11,
    9: 3,
    10: 8,
    11: 6,
}


def notes_to_anchor_intervals(anchor_note: int, notes: List[int]) -> List[int]:
    """
    return the anchor intervals of a list of notes.

    :param anchor_note:
    :param notes:
    :return:
    """
    return [note_to_anchor_interval(anchor_note, note) for note in notes]


def note_to_anchor_interval(anchor_note: int, note: int) -> int:
    """
    Given a note, and an anchor note, return the notes anchor interval

    :param anchor_note: int
    :param note: int
    :return: int
    """
    return note - anchor_note


def note_to_frequency(note):
    return 2 ** (note / 12) * constants.BASE_NOTE_FREQUENCY

def note_to_midi(note):
    """
    zero gets mapped to middle C which is 60
    :param note:
    :return:
    """
    return note + 60

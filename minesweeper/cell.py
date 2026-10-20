"""تمثيل مربع واحد في لوحة اللعبة."""

from dataclasses import dataclass


@dataclass
class Cell:
    """بيانات مربع واحد فقط، بدون أي منطق.

    Attributes:
        is_mine: هل فيه قنبلة؟
        is_revealed: هل انكشف؟
        is_flagged: هل عليه علم؟
        adjacent_mines: عدد القنابل في المربعات المجاورة (0 إلى 8).
    """

    is_mine: bool = False
    is_revealed: bool = False
    is_flagged: bool = False
    adjacent_mines: int = 0

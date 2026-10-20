"""الإعدادات والثوابت لكل المشروع.

أي رقم أو رمز أو مسار يتكرر في الكود يكون هنا، عشان نعدله من مكان واحد.
هذا الملف ما يستورد curses ولا rich، فيبقى المنطق منفصل عن الواجهة.
"""

LEVELS = {
    "easy": {"rows": 9, "cols": 9, "mines": 10},
    "medium": {"rows": 16, "cols": 16, "mines": 40},
    "hard": {"rows": 16, "cols": 30, "mines": 99},
}

DEFAULT_LEVEL = "easy"

HIDDEN_CHAR = "#"
FLAG_CHAR = "F"
MINE_CHAR = "*"
EMPTY_CHAR = " "

NUMBER_COLORS = {
    1: "blue",
    2: "green",
    3: "red",
    4: "magenta",
    5: "yellow",
    6: "cyan",
    7: "white",
    8: "white",
}

SCORES_PATH = "data/scores.json"
MAX_SCORES_PER_LEVEL = 5

REFRESH_MS = 100

CELL_WIDTH = 3
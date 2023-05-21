import dataclasses
import json
import random
from typing import List

r = random.Random()
r.seed(42)


# All 4 colors have to have the same possibility → each card has to be "rotated" 4 times to make the game fair

@dataclasses.dataclass
class Card:
    name: str

    action: str
    red: str
    green: str
    yellow: str
    blue: str

    id: str = None

    def rotate(self):
        self.red, self.green, self.yellow, self.blue = self.green, self.yellow, self.blue, self.red


def export(cards: List[Card], singular_cards: List[Card] = None, stat=True):
    if singular_cards is None:
        singular_cards = []

    cards_to_export = []
    ticker = 0

    for card in cards:
        for x in range(4):
            ticker += 1
            card.id = f"ID-{ticker}"
            card.name += f" {x + 1}"
            cards_to_export.append(dataclasses.asdict(card))
            card.rotate()

    for card in singular_cards:
        ticker += 1
        card.id = f"ID-{ticker}-O"
        cards_to_export.append(dataclasses.asdict(card))

    for _ in range(20):
        r.shuffle(cards_to_export)

    with open("src/components/cards.json", "w") as f:
        f.write(json.dumps(cards_to_export))

    if stat:
        means = {
            "action": 0,
            "red": 0,
            "green": 0,
            "yellow": 0,
            "blue": 0,
        }

        for card in cards_to_export:
            for k, v in card.items():
                if k in ["id", "name"]:
                    continue
                try:
                    v = int(v)
                except ValueError:
                    v = 0
                means[k] += v

        print(means)
        print(len(cards_to_export), "cards")


if __name__ == "__main__":
    export(
        [
            Card("One-Up", "±0", "+10", "-20", "-30", "±0"),
            Card("Number neighbours", "+8", "+15", "+15", "-15", "-15"),
            Card("Orthogonal", "-5", "-5", "+5", "-5", "+5"),
            Card("Flow", "+20", "-13", "-19", "-3", "-5"),
            Card("Burner", "+6", "-5", "+9", "+17", "-3"),
            Card("Sisters", "-10", "+9", "-9", "+7", "+7"),
            Card("Welcome", "+2", "-6", "-2", "+6", "-9"),
            Card("Password", "+1", "+2", "+3", "+4", "+5"),
            Card("Jack", "+20", "+20", "±0", "±0", "±0"),
            Card("Submarine", "-20", "-20", "±0", "±0", "±0"),
            Card("Chesterfield", "-18", "+1", "-13", "+14", "+19"),
            Card("Shinkansen", "+4", "+15", "+27", "+3", "-9"),
            Card("Born", "+5", "+9", "+10", "-1", "+17"),
            Card("Passing", "+12", "-4", "+1", "+3", "+9"),
            Card("Horses", "+12", "+17", "-2", "+14", "-5"),
            Card("Triumph", "+5", "-2", "-1", "+9", "+1"),
            Card("Visit", "-1", "+3", "-6", "+11", "+14"),
            Card("Ability", "-5", "+17", "+18", "-8", "+14"),
            Card("Present", "+11", "+9", "+10", "-5", "-4"),
            Card("Deal", "+7", "+10", "+19", "-4", "-1"),
            Card("Backgammon", "-7", "+10", "-8", "+17", "+5"),
            Card("Cassette", "+17", "+8", "-6", "+4", "-3"),
            Card("Detail", "-7", "+12", "+16", "+6", "+13"),
            Card("Plant", "+6", "+15", "-10", "-6", "-5"),
        ],
        [
            Card("Equilibrium", "+10", "+10", "+10", "+10", "+10"),
            Card("Equilibrium 2", "-10", "-10", "-10", "-10", "-10"),
            Card("Live", "±0", "±0", "±0", "±0", "±0"),
            Card("Tnt", "+4", "+4", "+4", "+4", "+4"),
        ]
    )

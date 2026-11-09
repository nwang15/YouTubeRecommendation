
import csv
from pathlib import Path

from model import YouTubeModel


# Find the main project folder
ROOT = Path(__file__).resolve().parents[2]
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)


def run_simulation(weight, condition):
    model = YouTubeModel(
        popularity_weight=weight,
        rng=42
    )

    rows = []

    for round_number in range(1, 11):
        model.step()

        new, established = model.get_exposure()

        rows.append({
            "round": round_number,
            "new_creator_exposure": new,
            "established_creator_exposure": established
        })

    filename = (
        f"{condition}_raw_00_exposure_by_round.csv"
    )

    filepath = OUTPUTS / filename

    with open(filepath, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "round",
                "new_creator_exposure",
                "established_creator_exposure"
            ]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n{condition.upper()} (weight={weight})")
    print("New creator exposure:", new)
    print("Established creator exposure:", established)
    print("Saved:", filepath)


run_simulation(0.3, "baseline")
run_simulation(0.7, "alternative")


import csv
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
OUTPUTS = ROOT / "outputs"


def create_chart(condition):
    filename = f"{condition}_raw_00_exposure_by_round.csv"

    rounds = []
    new_exposure = []
    established_exposure = []

    with open(OUTPUTS / filename, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rounds.append(int(row["round"]))
            new_exposure.append(
                int(row["new_creator_exposure"])
            )
            established_exposure.append(
                int(row["established_creator_exposure"])
            )

    plt.figure(figsize=(8, 5))

    plt.plot(
        rounds, new_exposure,
        marker="o", label="New Creators"
    )

    plt.plot(
        rounds, established_exposure,
        marker="o", label="Established Creators"
    )

    plt.xlabel("Recommendation Round")
    plt.ylabel("Cumulative Exposure")
    plt.title(
        f"{condition.capitalize()} Recommendation Exposure"
    )
    plt.legend()
    plt.grid(True)

    output_file = (
        OUTPUTS /
        f"{condition}_processed_00_exposure_by_round.png"
    )

    plt.savefig(output_file, dpi=150, bbox_inches="tight")
    plt.close()

    print("Saved:", output_file)


create_chart("baseline")
create_chart("alternative")

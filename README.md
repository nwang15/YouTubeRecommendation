YouTube Recommendation Exposure Simulation
1. Project Overview
This project investigates how adjusting the weight assigned to video popularity—within a simplified version of a YouTube-style recommendation system—affects the recommendation exposure received by new creators versus established creators.

Using Python and the Mesa framework, this project develops an agent-based model (ABM) to explore how recommendation mechanisms influence the distribution of exposure among creators by comparing outcomes under varying popularity-weighting scenarios.

This model uses synthetic data and does not represent YouTube’s actual recommendation algorithm.

2. Model Design

The model is implemented using Python and the Mesa framework and consists of the following key components:

- Agents: 6 simulated viewers, each with distinct interest preferences.

- Videos: 4 simulated videos—2 from new creators and 2 from established creators.

- Recommendation Rule: The system calculates a recommendation score based on a video's popularity and its relevance to a user's interests.

- Simulation Rounds: Each experiment consists of 10 rounds of recommendations.

- Output: The model records the cumulative number of recommendation exposures received by each of the two categories of creators.

Recommendation score formula:

Score = w × Popularity + (1 - w) × Relevance

Where:

- w represents the weight assigned to popularity.

- Popularity represents the popularity of a video.

- Relevance represents the degree of alignment between a video and a user's interests.

In each round, every viewer receives one recommended video, and the exposure count for that video increases by 1.

Baseline:

Popularity Weight = 0.3
Relevance Weight = 0.7

Alternative:

Popularity Weight = 0.7
Relevance Weight = 0.3

Both experimental setups use the same simulated audience, video data, recommendation rules, and number of simulation rounds; only the Popularity Weight is varie

4. How to Run
First, install the Python dependencies required for the project:

py -m pip install -r requirements.txt

Run the simulations for both the Baseline and Alternative scenarios:

py src/project_model/run.py

Generate charts for the simulation results:

py src/project_model/plot.py

Once the execution is complete, the generated CSV data files and PNG charts will be saved in the outputs/ folder.

5. Initial Results

Condition	New Creators	Established Creators
Baseline	20	            40
Alternative	0	            60

Increasing the popularity weight from 0.3 to 0.7 reduced exposure for new creators in this synthetic scenario.

Under the Baseline condition, new creators received 20 recommendation exposures—accounting for 33.3% of the total—while established creators received 40, accounting for 66.7%.

Under the Alternative condition, new creators received 0 recommendation exposures, whereas established creators received all 60 exposures.

In the current simulation, increasing the "Popularity Weight" from 0.3 to 0.7 leads to further concentration of recommendation exposures toward established creators.

These results reflect the model's performance only under specific synthetic data and rules; they cannot be used to infer the behavior of the actual YouTube recommendation system.

6. Source Example
This project draws conceptual inspiration from the Schelling Segregation model provided by the Mesa framework.

The Schelling model demonstrates how simple individual behavioral rules can lead to aggregate-level distributional disparities.

There is a parallel here to this project: even when a recommendation system employs simple ranking rules, it can result in recommendation exposure becoming concentrated among a specific subset of creators.

However, the underlying mechanisms of the two models differ:

- The Schelling model focuses primarily on the movement and clustering of agents within a spatial environment.

- This project focuses on the ranking of video recommendations and the allocation of exposure.

The original Schelling example is located in src/source_example/.

The YouTube recommendation model developed for this project is located in src/project_model/. It is implemented independently using Mesa’s Agent and Model classes, rather than by directly modifying the movement rules of the Schelling model.

7. Limitations

This project has the following limitations:

The model is small in scale, featuring only 6 simulated viewers and 4 videos.

All data used are synthetic rather than actual data from YouTube.

User interests and video popularity remain constant throughout the simulation.

Each viewer receives only one recommended video per round.

The model does not account for factors such as viewing history, likes, comments, or watch duration.

The recommendation rules are simplified, manually defined formulas and do not represent YouTube’s actual recommendation algorithm.

Consequently, the model’s results can only be used to analyze exposure distribution under the specified rules and parameters; they cannot be directly generalized to real-world platforms.

8. Next Steps

Future iterations of this project could expand the model by:

Increasing the number of simulated viewers and videos.

Introducing a more diverse range of user interests and video characteristics.

Incorporating user viewing or interaction behaviors.

Investigating whether exposure levels, in turn, influence video popularity.

Comparing a broader set of "popularity weight" conditions.

Conducting multiple simulation runs to verify whether the results remain consistent across different initial conditions.

These enhancements would facilitate further research into how recommendation mechanisms affect the exposure opportunities available to different types of creators.



## DEL03 Updates

The DEL03 submission builds upon the existing DEL02
computational model and baseline/alternative comparison.

### Changes Since DEL02

- Added evidence documentation in `docs/evidence/`.
- Documented the synthetic viewer and video input data.
- Documented the recommendation scoring rule and assumptions.
- Added a YouTube homepage screenshot as platform context.
- Added an ecosystem map to clarify actors, relationships,
  recommendation flows, and computational boundaries.
- Expanded the interpretation of exposure distribution,
  potential consequences, trade-offs, and limitations.

### Evidence and Documentation

| File | Description |
|---|---|
| `docs/evidence/synthetic_inputs.csv` | Synthetic model inputs (E3) |
| `docs/evidence/recommendation_rule.md` | Scoring rule and experimental conditions (E4) |
| `docs/evidence/youtube_homepage.png` | Observed YouTube homepage interface (E5) |
| `docs/figures/ecosystem_map.png` | Ecosystem map and computational boundary |

### Model and Comparison

The original DEL02 model and experimental conditions
are retained in DEL03.

- Baseline popularity weight: 0.3
- Alternative popularity weight: 0.7
- Number of viewers: 6
- Number of videos: 4
- Simulation rounds: 10

The DEL03 updates focus on evidence documentation,
representation transparency, and interpretation rather
than changing the computational model.

### Reproducibility

Run the following commands from the project root:

```bash
py -m pip install -r requirements.txt
py src/project_model/run.py
py src/project_model/plot.py
```

All generated outputs are stored in the `outputs/` directory.

### Research Boundary

This project uses synthetic data and an illustrative
recommendation rule. It does not reproduce YouTube's
actual recommendation algorithm.

The original DEL02 materials and release are retained
for reference.

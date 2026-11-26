
# Simplified Recommendation Scoring Rule

## Purpose

This rule is designed to investigate how popularity weight
affects recommendation exposure for new and established creators.

## Relevance Calculation

Relevance = 1 - abs(Viewer Interest - Video Topic)

Viewer interest and video topic are represented by values
between 0 and 1.

## Recommendation Score

Score = w * Popularity + (1 - w) * Relevance

Where:

- w: popularity weight
- Popularity: initial video popularity
- Relevance: similarity between viewer interest and video topic

## Recommendation Process

1. Calculate the recommendation score for each video.
2. Select the video with the highest score.
3. Increase the selected video's exposure count by 1.
4. Repeat for every viewer in each simulation round.

## Experimental Conditions

| Parameter | Baseline | Alternative |
|---|---:|---:|
| Popularity Weight | 0.3 | 0.7 |
| Relevance Weight | 0.7 | 0.3 |
| Number of Viewers | 6 | 6 |
| Number of Videos | 4 | 4 |
| Simulation Rounds | 10 | 10 |

Only the popularity weight is independently changed
between the two conditions.

## Assumptions and Limitations

- All input data are synthetic.
- Viewer interests remain unchanged.
- Video popularity remains unchanged.
- Each viewer receives one recommendation per round.
- Exposure represents recommendation events, not actual views.
- The scoring rule is illustrative and does not reproduce
  YouTube's actual recommendation algorithm.

## Source

Project-defined modelling specification, 2026.

Implementation: src/project_model/model.py

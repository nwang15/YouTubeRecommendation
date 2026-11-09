
from mesa import Agent, Model


class ViewerAgent(Agent):
    def __init__(self, model, interest):
        super().__init__(model)
        self.interest = interest

    def receive_recommendation(self):
        videos = self.model.videos

        def score(video):
            popularity = video["popularity"]
            relevance = 1.0 - abs(
                self.interest - video["topic"]
            )

            return (
                self.model.popularity_weight * popularity
                + (1 - self.model.popularity_weight) * relevance
            )

        recommended_video = max(videos, key=score)
        recommended_video["exposure"] += 1


class YouTubeModel(Model):
    def __init__(self, popularity_weight=0.3, rng=42):
        super().__init__(rng=rng)

        self.popularity_weight = popularity_weight
        self.round_number = 0

        # Synthetic video data, not real YouTube data
        self.videos = [
             {
                "creator": "new",
                "popularity": 0.2,
                "topic": 0.1,
                "exposure": 0,
            },
            {
                "creator": "new",
                "popularity": 0.3,
                "topic": 0.9,
                "exposure": 0,
            },
            {
                "creator": "established",
                "popularity": 0.8,
                "topic": 0.4,
                "exposure": 0,
            },
            {
                "creator": "established",
                "popularity": 0.9,
                "topic": 0.6,
                "exposure": 0,
            },
        ]

        self.viewers = [
            ViewerAgent(self, interest)
            for interest in [0.1, 0.25, 0.4, 0.6, 0.75, 0.9]
        ]

    def step(self):
        self.round_number += 1

        for viewer in self.viewers:
            viewer.receive_recommendation()

    def get_exposure(self):
        new_exposure = sum(
            video["exposure"]
            for video in self.videos
            if video["creator"] == "new"
        )

        established_exposure = sum(
            video["exposure"]
            for video in self.videos
            if video["creator"] == "established"
        )

        return new_exposure, established_exposure


if __name__ == "__main__":
    model = YouTubeModel(popularity_weight=0.3)

    for _ in range(10):
        model.step()

    new, established = model.get_exposure()

    print("Simulation completed!")
    print("Rounds:", model.round_number)
    print("New creator exposure:", new)
    print("Established creator exposure:", established)

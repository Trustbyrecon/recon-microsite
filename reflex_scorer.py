class ReflexScorer:
    def __init__(self):
        self.score = 0.0

    def compute(self, input_signal):
        # Placeholder logic for trust score
        self.score = 0.82 if input_signal else 0.0
        return self.score

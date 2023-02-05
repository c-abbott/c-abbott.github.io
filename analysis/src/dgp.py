from dataclasses import dataclass

import numpy as np
import pandas as pd


class dgp_steps_experiment:
    """
    Data Generating Process: Step counter experiment
    """

    def __init__(self, N, p, alpha, beta, gamma, delta, steps_stddev, seed=42):
        """
        Initialize DGP
        """
        self.N: int = N
        self.p: float = p
        self.alpha: float = alpha
        self.beta: float = beta
        self.gamma: float = gamma
        self.delta: float = delta
        self.seed: int = seed
        self.steps_stddev: float = steps_stddev

    def generate_data(self):
        """
        Generate data
        """
        np.random.seed(self.seed)

        # Experiment units
        i = np.arange(1, self.N + 1)
        # Treatment assignment
        t = np.random.binomial(1, self.p, self.N)

        # Create avg_daily_steps metric before and after treatment
        y_pre = (
            self.alpha + self.beta * t + np.random.normal(0, self.steps_stddev, self.N)
        )
        y_post = (
            y_pre
            + self.gamma
            + self.delta * t
            + np.random.normal(0, self.steps_stddev, self.N)
        )

        # Create experiment data frame
        df = pd.DataFrame({"i": i, "is_treatment": t, "y_pre": y_pre, "y_post": y_post})

        return df

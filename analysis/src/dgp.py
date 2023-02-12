from dataclasses import dataclass
import numpy as np
import pandas as pd

class dgp_steps_experiment:
    """
    Data Generating Process: Step counter experiment
    """

    def __init__(self, N, p, alpha, beta, gamma, delta, steps_stddev, num_users, num_pre_experiment_points=14, num_post_experiment_points=28, seed=42):
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
        self.num_users = num_users
        self.num_pre_experiment_points = num_pre_experiment_points
        self.num_post_experiment_points = num_post_experiment_points

    def generate_pre_experiment_data(self):
        np.random.seed(self.seed)

        # Initialize an empty list to store dataframes for each user
        df_list = []

        # Loop over the number of users
        for i in range(self.N):
            user_id = np.ones(self.num_pre_experiment_points) * int(i)

            sigma_user = np.random.randint(low=1000, high=2000, size=1)
            
            y_pre = (
                self.alpha + np.random.normal(0, sigma_user, self.num_pre_experiment_points)
            )

            days = np.arange(-1*self.num_pre_experiment_points, 0)


            df = pd.DataFrame({'day_in_experiment': days, 'user_id': user_id, 'y_pre': y_pre})


            df_list.append(df)
        # Concatenate all the dataframes in the list into a single dataframe
        result = pd.concat(df_list)

        # Sort the dataframe by date and user_id
        result = result.sort_values(by=['user_id', 'day_in_experiment'])

        return result





    # def generate_data(self):
    #     """
    #     Generate data
    #     """
    #     np.random.seed(self.seed)

    #     # Initialize an empty list to store dataframes for each user
    #     df_list = []
        
    #     # Loop over the number of users
    #     for i in range(self.N):
    #         # Experiment units
    #         user_id = np.ones(self.num_points) * i
    #         # Treatment assignment
    #         t = np.random.binomial(1, self.p) * np.ones(self.num_points)

    #         # Create avg_daily_steps metric before and after treatment
    #         y_pre = (
    #             self.alpha + self.beta * t + np.random.normal(0, self.steps_stddev, self.num_points)
    #         )
    #         y_post = (
    #             y_pre
    #             + self.gamma
    #             + self.delta * t
    #             + np.random.normal(0, self.steps_stddev, self.num_points)
    #         )

    #         # Generate a list of dates
    #         dates = pd.date_range('2022-01-01', periods=self.num_points)

    #         # Combine the dates, user_id, treatment status and step count data into a dataframe
    #         df = pd.DataFrame({'date': dates, 'user_id': user_id, 'is_treatment': t, 'y_pre': y_pre, 'y_post': y_post})

    #         # Set the date column as the index of the dataframe
    #         df = df.set_index('date')
            
    #         # Add the dataframe for the current user to the list of dataframes
    #         df_list.append(df)

    #     # Concatenate all the dataframes in the list into a single dataframe
    #     result = pd.concat(df_list)

    #     # Sort the dataframe by date and user_id
    #     result = result.sort_values(by=['date', 'user_id'])

    #     return result

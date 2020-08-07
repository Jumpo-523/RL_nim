import pandas as pd
import numpy as np
import random
import itertools

#action = 3
# reward = 1 if y==2 else 0
class ContextualArms(object):
    def __init__(self,
                 n_action,
                 max_n_sim, 
                 X, y=None,
                 arms=None,
                 n_features=4,
                 is_logit=False
                ):
        self.X = X.copy()
        self.y = y.copy()
        self.arms = arms
        self.n_action = n_action
        self.max_n_sim = max_n_sim
        self.t_count = 0
        self.history_idx = []
        self.is_logit = is_logit
    def __len__(self):
        return self.n_action
    def __getitem__(self, index):
        return self.X[index, :], self.y[index]
        pass
    def reset(self):
        self.t_count = 0

    def draw(self):
        assert self.X is not None  and self.y is not None
        res = {}
        retrieve_indices = []
        for a in range(1, self.n_action+1):
            arm_a_idx_list = list(np.where(self.arms == a)[0])
            idx_a = random.sample(arm_a_idx_list, 1)
            retrieve_indices.append(idx_a)
        self._candidates_idx = list(itertools.chain.from_iterable(retrieve_indices))
        res = self.X[self._candidates_idx, :]

        return res
    
    def best_arms(self):
        if self.is_logit:
            return np.where(self.y[self._candidates_idx] == 1)[0]
        else: # for normal contextual bandit.
            return ds.groupby("arm").mean()["reward"].idxmax()
    def get_reward(self, index):
        """
        rewardが0,1の値をとる確率変数でわかりずらかったため、試しにdetermined valued rewardを与える。
        """
        self.history_idx.append(self._candidates_idx[index])
        if self.is_logit:
            return (ds.groupby("arm").mean()["reward"]*100).iloc[index]
        else:
            return self.y[self._candidates_idx[index]]
from typing import Tuple
from functools import reduce

def calculate_stars_and_forks(repos : list) -> Tuple[int,int]:
    total_forks = reduce(lambda x,y : x.stargazers_count + y.stargazers_count,repos)

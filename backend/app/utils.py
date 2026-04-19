from typing import Tuple
from app.schemas import GitHubRepo,LanguageBreakdown
from collections import Counter

def calculate_stars_and_forks(repos : list[GitHubRepo]) -> Tuple[int,int]:
    """Calculates the total stars and forks for original works."""
    total_stars ,total_forks = 0, 0
    original_repos = [repo for repo in repos if not repo.fork] 
    
    for r in original_repos:
        total_forks +=  r.forks
        total_stars +=  r.stars

    return total_stars,total_forks

def calculate_language_breakdown(repos : list[GitHubRepo]) -> list[LanguageBreakdown]:
    """"Optimized language analysis by aggregating primary language data and avoiding redundant API calls."""

    original_repos = [repo for repo in repos if not repo.fork]
    if not original_repos:
        return []

    lang_counts = Counter([r.language for r in original_repos if r.language])  # Count occurrences of each language
    total_langs = n = sum(lang_counts.values())

    breakdown = []
    for lang, count in lang_counts.items():
        percentage = round((count / n) * 100, 2)  #each lang's % calculation
        breakdown.append(LanguageBreakdown(language=lang, percentage=percentage))

    return sorted(breakdown, key=lambda l: l.percentage, reverse=True) # Sort by percentage descending
    
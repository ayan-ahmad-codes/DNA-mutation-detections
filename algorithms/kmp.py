# algorithms/kmp.py
import re

def normalize(seq: str) -> str:
    """
    Cleans DNA input for exact matching.
    - Uppercase
    - Removes all whitespace
    """
    return re.sub(r'\s+', '', seq.upper())


def compute_lps(pattern: str):
    """
    Computes Longest Prefix Suffix (LPS) array
    Correctly handles overlapping patterns
    """
    lps = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    return lps


def kmp_search(text: str, pattern: str):
    """
    Returns all starting indices of pattern in text
    Supports overlapping matches
    """
    text = normalize(text)
    pattern = normalize(pattern)

    if not pattern or len(pattern) > len(text):
        return []

    lps = compute_lps(pattern)
    i = j = 0
    matches = []

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]   # enables overlapping

        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches

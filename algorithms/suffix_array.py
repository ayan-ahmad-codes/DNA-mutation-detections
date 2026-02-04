def build_suffix_array(text):
    suffixes = [(text[i:], i) for i in range(len(text))]
    suffixes.sort()
    return [idx for (_, idx) in suffixes]


def suffix_search(text, pattern, suffix_array):
    matches = []
    for idx in suffix_array:
        if text[idx:idx+len(pattern)] == pattern:
            matches.append(idx)
    return matches

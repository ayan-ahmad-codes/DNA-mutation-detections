def detect_mutations(dna, pattern):
    """
    Detect mutation positions by direct comparison.
    """
    mutations = []
    min_len = min(len(dna), len(pattern))

    for i in range(min_len):
        if dna[i] != pattern[i]:
            mutations.append(i)

    return mutations


def mutation_percentage(mutation_count, dna_length):
    if dna_length == 0:
        return 0.0
    return round((mutation_count / dna_length) * 100, 2)

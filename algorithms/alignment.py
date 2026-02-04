def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-1):
    """
    Needleman–Wunsch global alignment score.
    
    seq1 : Reference DNA sequence
    seq2 : Pattern / query DNA sequence
    """

    n = len(seq1)
    m = len(seq2)

    # Create scoring matrix
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize first row and column with gap penalties
    for i in range(1, n + 1):
        dp[i][0] = i * gap
    for j in range(1, m + 1):
        dp[0][j] = j * gap

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                score_diag = dp[i - 1][j - 1] + match
            else:
                score_diag = dp[i - 1][j - 1] + mismatch

            score_up = dp[i - 1][j] + gap
            score_left = dp[i][j - 1] + gap

            dp[i][j] = max(score_diag, score_up, score_left)

    # Final alignment score
    return dp[n][m]

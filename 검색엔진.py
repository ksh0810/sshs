def levenshtein(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )
    return dp[n][m]

def get_similarity(s1, s2):
    distance = levenshtein(s1, s2)
    max_len = max(len(s1), len(s2))
    return 1 - distance / max_len if max_len > 0 else 1.0

def suggest(user_input, locations, threshold=0.6):
    suggestions = []
    for loc in locations:
        score = get_similarity(user_input, loc)
        if score >= threshold:
            suggestions.append((loc, round(score, 2)))
    suggestions.sort(key=lambda x: x[1], reverse=True)
    return suggestions

locations=['도서관','여자기숙사','우암공통강의실','체육관'] 
print(suggest(input(),locations))
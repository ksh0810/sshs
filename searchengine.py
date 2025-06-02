def longest_common_substring(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0

    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                max_len = max(max_len, dp[i + 1][j + 1])
    return max_len

def get_similarity(s1, s2):
    lcs_len = longest_common_substring(s1, s2)
    similarity = 1 - 1 / (lcs_len + 1)  # 비선형 함수
    return similarity

def suggest(user_input, locations, threshold=0.2):
    suggestions = []
    for loc in locations:
        score = get_similarity(user_input, loc)
        if score >= threshold:
            suggestions.append((loc, round(score, 2)))
    suggestions.sort(key=lambda x: x[1], reverse=True)
    try:
        return list(map(lambda x: x[0],suggestions[:5]))
    except:
        return ['진로상담실','수학강의실4','화학강의실1','준비실','지구과학강의실1']
def mostsimilarity(user_input,locations,threshold=0.2):
    return suggest(user_input,locations,threshold=0.2)[0]
####예외처리 해라. indexerror하셈



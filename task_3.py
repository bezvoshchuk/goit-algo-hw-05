import timeit

# Функції пошуку підрядка

def naive_search(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            return True
    return False

def kmp_search(text, pattern):
    def compute_prefix(pattern):
        prefix = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[j] != pattern[i]:
                j = prefix[j-1]
            if pattern[j] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix

    prefix = compute_prefix(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            return True
    return False

def bm_search(text, pattern):
    last_occurrence = {}
    for i, char in enumerate(pattern):
        last_occurrence[char] = i

    n = len(text)
    m = len(pattern)
    i = m - 1
    if i > n - 1:
        return False

    j = m - 1
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return True
            else:
                i -= 1
                j -= 1
        else:
            if text[i] not in last_occurrence:
                i += m
            else:
                shift = j - last_occurrence[text[i]]
                i += max(1, shift)
            j = m - 1
    return False

def rk_search(text, pattern):
    def hash_function(string, modulus):
        hash_value = 0
        for char in string:
            hash_value = (hash_value * 256 + ord(char)) % modulus
        return hash_value

    n = len(text)
    m = len(pattern)
    if m > n:
        return False

    pattern_hash = hash_function(pattern, 101)
    text_hash = hash_function(text[:m], 101)
    if pattern_hash == text_hash and text[:m] == pattern:
        return True

    high_order = (256 ** (m - 1)) % 101
    for i in range(1, n - m + 1):
        text_hash = (256 * (text_hash - ord(text[i - 1]) * high_order) + ord(text[i + m - 1])) % 101
        if pattern_hash == text_hash and text[i:i+m] == pattern:
            return True
    return False

# Зчитування текстових файлів і підрядків

with open('article_1.txt', encoding="ISO-8859-1") as file:
    text1 = file.read()

with open('article_2.txt', encoding="ISO-8859-1") as file:
    text2 = file.read()

pattern1_exist = "ваш_підрядок_1_існуючий"
pattern1_non_exist = "ваш_підрядок_1_невигаданий"
pattern2_exist = "ваш_підрядок_2_існуючий"
pattern2_non_exist = "ваш_підрядок_2_невигаданий"

# Вимірювання часу виконання кожного алгоритму для кожного підрядка

naive_time1_exist = timeit.timeit(lambda: naive_search(text1, pattern1_exist), number=100)
kmp_time1_exist = timeit.timeit(lambda: kmp_search(text1, pattern1_exist), number=100)
bm_time1_exist = timeit.timeit(lambda: bm_search(text1, pattern1_exist), number=100)
rk_time1_exist = timeit.timeit(lambda: rk_search(text1, pattern1_exist), number=100)

naive_time1_non_exist = timeit.timeit(lambda: naive_search(text1, pattern1_non_exist), number=100)
kmp_time1_non_exist = timeit.timeit(lambda: kmp_search(text1, pattern1_non_exist), number=100)
bm_time1_non_exist = timeit.timeit(lambda: bm_search(text1, pattern1_non_exist), number=100)
rk_time1_non_exist = timeit.timeit(lambda: rk_search(text1, pattern1_non_exist), number=100)

naive_time2_exist = timeit.timeit(lambda: naive_search(text2, pattern2_exist), number=100)
kmp_time2_exist = timeit.timeit(lambda: kmp_search(text2, pattern2_exist), number=100)
bm_time2_exist = timeit.timeit(lambda: bm_search(text2, pattern2_exist), number=100)
rk_time2_exist = timeit.timeit(lambda: rk_search(text2, pattern2_exist), number=100)

naive_time2_non_exist = timeit.timeit(lambda: naive_search(text2, pattern2_non_exist), number=100)
kmp_time2_non_exist = timeit.timeit(lambda: kmp_search(text2, pattern2_non_exist), number=100)
bm_time2_non_exist = timeit.timeit(lambda: bm_search(text2, pattern2_non_exist), number=100)
rk_time2_non_exist = timeit.timeit(lambda: rk_search(text2, pattern2_non_exist), number=100)

# Виведення результатів

print("Час виконання для тексту 1 з наявним підрядком:")
print("Наївний алгоритм:", naive_time1_exist)
print("КМП:", kmp_time1_exist)
print("Боєр-Мур:", bm_time1_exist)
print("Рабін-Карп:", rk_time1_exist)

print("Час виконання для тексту 1 з невигаданим підрядком:")
print("Наївний алгоритм:", naive_time1_non_exist)
print("КМП:", kmp_time1_non_exist)
print("Боєр-Мур:", bm_time1_non_exist)
print("Рабін-Карп:", rk_time1_non_exist)

print("Час виконання для тексту 2 з наявним підрядком:")
print("Наївний алгоритм:", naive_time2_exist)
print("КМП:", kmp_time2_exist)
print("Боєр-Мур:", bm_time2_exist)
print("Рабін-Карп:", rk_time2_exist)

print("Час виконання для тексту 2 з невигаданим підрядком:")
print("Наївний алгоритм:", naive_time2_non_exist)
print("КМП:", kmp_time2_non_exist)
print("Боєр-Мур:", bm_time2_non_exist)
print("Рабін-Карп:", rk_time2_non_exist)
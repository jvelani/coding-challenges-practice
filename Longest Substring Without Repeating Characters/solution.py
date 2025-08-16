def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    right = 1
    left = 0
    max_len = 0
    while right < len(s):
        window = s[left:right]
        if s[right] not in window:
            right +=1
            max_len = max(max_len, right-left)
        else:
            left +=1
            right = left + 1
    return max_len

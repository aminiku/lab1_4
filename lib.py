def count_common_elements(*lists):
    if not lists:
        return 0
    common = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)
    return len(common)
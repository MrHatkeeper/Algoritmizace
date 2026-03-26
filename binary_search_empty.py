
def binary_search_recursive(ordered_list: list, value: int) -> int:
    """
    Perform a recursive binary search on a sorted list.

    Parameters:
        ordered_list (list): Sorted input list.
        value: Value to search for.

    Returns:
        int: Index of the value if found, otherwise -1.
    """
    if value < ordered_list[0] or value > ordered_list[-1]:
        return -1
    return _binSearchRec(ordered_list, value, len(ordered_list))

def _binSearchRec(ordered_list: list, value: int, max: int, min: int = 0) -> int:
    pos = (min + max) // 2
    if value == ordered_list[pos]:
        return pos
    if min+1 == max:
        return -1
    if value < ordered_list[pos]:
        return _binSearchRec(ordered_list, value, pos, min)
    return _binSearchRec(ordered_list, value, max, pos)

def binary_search(ordered_list: list, value: int) -> int:
    """
    Perform an iterative binary search on a sorted list.

    Parameters:
        ordered_list (list): Sorted input list.
        value: Value to search for.

    Returns:
        int: Index of the value if found, otherwise -1.
    """
    if value < ordered_list[0] or value > ordered_list[-1]:
        return -1
    min = 0
    max = len(ordered_list)

    while True:
        pos = (min + max) // 2
        if value == ordered_list[pos]:
            return pos
        if min+1 == max:
            return -1
        if value < ordered_list[pos]:
            max = pos
        else:
            min = pos


def testBinRecSearch():
    l = list()
    for i in range(10):
        l.append(i)
    print("Větší, než max číslo")
    print(l, "| hledám: 999", binary_search_recursive(l, 999))
    print("Menší, než min číslo")
    print(l, "| hledám: -999", binary_search_recursive(l, -999))
    print("Chybjející prvek v listu")
    l.remove(4)
    print(l, "| hledám: 4", binary_search_recursive(l, 4))
    print("ostatní")
    for x in l:
        print(l, "|",x, binary_search_recursive(l, x))

def testBinSearch():
    l = list()
    for i in range(10):
        l.append(i)
    print("Větší, než max číslo")
    print(l, "| hledám: 999", binary_search(l, 999))
    print("Menší, než min číslo")
    print(l, "| hledám: -999", binary_search(l, -999))
    print("Chybjející prvek v listu")
    l.remove(4)
    print(l, "| hledám: 4", binary_search(l, 4))
    print("ostatní")
    for x in l:
        print(l, "| hledám:",x, binary_search(l, x))
testBinRecSearch()
testBinSearch()


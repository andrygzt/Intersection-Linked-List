


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    currentA = headA
    currentB = headB

    while currentA != None:
        while currentB != None:
            if currentB == currentA:
                return currentB
            currentB = currentB.next
        currentA = currentA.next
        currentB = headB
    return None
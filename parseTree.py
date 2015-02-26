from collections import defaultdict
class Node():
    def __init__(self, head = None, data = None, nextel = None):
        self.head = head
        self.data = data
        self.nextel = nextel

def parseChildren(s):
    l = 0
    r = 0
    ex = 0
    if len(s) == 3:
        return ['!','!']
    else:
        for i in range(len(s)):
            if s[i] == '!':
                ex += 1
            if r == 0 and l == 0 and ex == 1:
                return ['!',s[i+2:]]
            if s[i] == '(':
                l += 1
            if s[i] == ')':
                r += 1
            if l != 0 and r != 0 and r == l:
                child = s[:i+1]
                return [child, s[i+2:]]

def stripParens(s):
    stripped = s[1:-1]
    return stripped

#string -> [string]
#'(a,(b),(c))' -> {'parent':['child1', 'child2']}
def getFamily(s):
    # if child inputted to be parsed equals none, return
    if s == '!':
        return '!'
    stripS = stripParens(s)
    parent = [stripS[0]]
    childList = parseChildren(stripS[2:])
    return parent + childList

def hookUp(s):
    def _hookUp(s):
        fam = getFamily(s)
        if (fam != '!'):
            currNode, leftStr, rightStr = fam
            leftNode = leftStr[1] if len(leftStr) > 1 else '!'
            rightNode = rightStr[1] if len(rightStr) > 1 else '!'
            famDict[currNode] = [leftNode, rightNode]
            _hookUp(leftStr)
            _hookUp(rightStr)

    famDict = dict()
    _hookUp(s)
    return famDict

#assert(hookUp('(a,!,!)') == {'a':['','']})
#assert(hookUp('(a,(b,!,!),!)', {}) == {'a':['b','!'],'b':['!','!']})
#assert(stripParens('(a)') == 'a')
#assert(parseChildren('(ab,c(d,e(f))),(dasf,dasf)')
assert(hookUp('(a,(b,!,(c,!,!)),(d,(e,!,!),!))') == {'a':['b','d'],'b':['!','c'],'c':['!','!'],'d':['e','!'],'e':['!','!']})
print hookUp('(a,(b,!,(c,!,!)),(d,(e,!,!),!))')
#assert(matchParen('(a,!,!)') == ['a','',''])
#assert(matchParen('(a,(b,!,!),!)') == ['a','(b,!,!)',''])
#assert(matchParen('(a,!,(b,!,!))') == ['a','','(b,!,!)'])
#assert(matchParen('(a,(b,!,(c,!,!)),(d,(e,!,!),!))')

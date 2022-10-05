from queue import LifoQueue

def isValid(s: str) -> bool:
    q = LifoQueue()
    map_dict = {'(':')', '{':'}', '[':']'}
    count = 0
    for i in range(len(s)):
        if s[i] in map_dict.keys():
            q.put(s[i])
            count += 1
        elif s[i] in map_dict.values() and count >= 1:
            val = q.get()
            count -= 1
            if not s[i] == map_dict.get(val):
                return False
        else:
            return False
    if q.qsize() == 0:
        return True
    else:
        return False

print(isValid('([])'))



















#         else:
#             val = q.get()
#             print(val)
#             # if q.qsize() == 0 and s[i] in map_dict.values():
#             #     return False
#             # if q.qsize() != 0 and s[i] != map_dict.get(q.get()):
#             #     return False
#             # else:
#             #     print('yes')
#             #     return True
#     print(q.qsize())
#     if q.qsize() == 0:
#         return True
#     else:
#         return False

# print(isValid(')'))
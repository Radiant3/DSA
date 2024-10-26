def groupAnagrams(strs):
    if len(strs) == 0 or len(strs) == 1:
        return [strs]

    sortedDic = {}

    for idx in range(len(strs)):
        sortedWord = ''.join(sorted(strs[idx]))

        if sortedWord in sortedDic:
            lst = sortedDic[sortedWord]
            print(lst)
            lst.append[strs[idx]]
            print()
            sortedDic[sortedWord] = lst
        
        else:
            sortedDic[sortedWord] = [strs[idx]]
            

    result = []
    for value in sortedDic.values():
        result.append(value)
    
    return result

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))
    
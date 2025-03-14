def mergeAlternately(word1, word2):
        merged = []
        a,b = 0,0
        l1,l2 = len(word1), len(word2)
        while a < l1 or b < l2:
            if a < l1:
                merged.append(word1[a])
                a+=1
            if b < l2:
                merged.append(word2[b])
                b+=1
        return "".join(merged)

merged_word = mergeAlternately("abc", "pqr")
print(merged_word) # apbqcr
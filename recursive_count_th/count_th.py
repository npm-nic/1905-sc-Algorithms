'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# # --> this is how i originally did it until i saw 'single-parameter' constraint above
# def count_th(word, counter = 0):
#     word_length = len(word)
#     if word_length <= 1: # base-case: stop when word_length <= 1 (b/c 'th' is two characters)
#         return counter
#     if word[:2] == "th":
#         counter += 1
#     return count_th(word[1:], counter)

# # --> another way to do it?  ... using baked in count()
# def count_th(word):
#     return word.count('th')

word1 = 'thasnthadnth'
word2 = '1231241'

def count_th(word):
    if len(word) <= 1: # base-case: stop when word_length <= 1 (b/c 'th' is two characters)
        return 0
    # if first two letters we are looking at are 'th'
    # --> return '1' (because 'th' occurs there)
    # --> plus recursively run count_th on rest of word
    #   --> starting at index 2 bc we know word[1] is 'h'
    if word[0:2] == 'th':
        return 1 + count_th(word[2:])
    else: # 'th' does not occur at word[0] - word[1], so start again at word[1]
        return count_th(word[1:])



print(count_th(word1), count_th(word2)) # should be --> 3 0 
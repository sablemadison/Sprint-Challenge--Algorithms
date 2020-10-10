'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    substring = 'th'
    if substring in word:
        remove = word.replace(substring, 'x', 1)
        count += 1
        return count + count_th(remove)
    else:
        return 0






    # check string for 'th'
    # if contains 'th' increment count
    # return count
    # repeat

    
    

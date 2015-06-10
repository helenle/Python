# Huyen Le


def collect_vowels(s):
    '''
    (s) => str
    collect_vowels("Happy Anniversary!")
    'aAiea'
    collect_vowels("xyz!")
    ''
    '''
    vowels = ''
    for char in s:
        if char in 'aeiuoAEIUO':
            vowels += char
    return vowels



def count_vowels(s):
        count = 0
        #s = s.lower()
        for char in s:
            if char in 'aeiuoAEIUO':
                count += 1
        return count
    

#count_vowels("Happy Anniversary")
#5

def count_char(string):
    dictionary = {}
    for char in string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[0]))
    print(sorted_dict)


count_char('Happiness')
count_char('smiles')

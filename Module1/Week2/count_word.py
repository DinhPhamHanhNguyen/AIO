def word_count(file_path):
    word_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.lower().strip().split()
            for word in words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
            sorted_dict = dict(
                sorted(word_dict.items(), key=lambda item: item[0]))

    items = sorted_dict.items()
    for key, value in items:
        print(f"'{key}'': {value}")


file_path = 'P1_data.txt'
word_count(file_path)

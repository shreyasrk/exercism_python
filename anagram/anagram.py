def detect_anagrams(word, list_of_possible_anagrams):
	result_list = []
	for possible_word in list_of_possible_anagrams:
		if word.lower() != possible_word.lower() and len(word) == len(possible_word) and sorted(list(word.lower())) == sorted(list(possible_word.lower())):
			result_list.append(possible_word)

    return result_list

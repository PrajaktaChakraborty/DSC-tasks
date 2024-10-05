def sort_by_word_length(sentence):
    words = sentence.split()
    
    sorted_words = sorted(words, key=len)
    
    return " ".join(sorted_words)

input_sentence = "This is a cool sentence"
output_sentence = sort_by_word_length(input_sentence)
print(output_sentence)
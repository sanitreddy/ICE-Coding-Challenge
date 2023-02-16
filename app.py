from collections import Counter

number_of_words = 0
number_of_letters = 0
number_of_paragraphs= 1
number_of_vowels = 0
vowels = "AaEeIiOoUu"
chapter_file = open('chapter1.txt')
lines = chapter_file.readlines()[3:]

for line in lines:
    words = line.split()
    number_of_words += len(words)
    
    if line == '\n':
        number_of_paragraphs += 1
    for word in words:
        number_of_letters += len(word)
        for letters in word:
            if(letters in vowels):
                number_of_vowels += 1

    
print("Paragraphs:", number_of_paragraphs)
print("Lines:", len(lines))
print("Words:", number_of_words)
print("Letters:", number_of_letters)
print("Vowels:",number_of_vowels)
print("Consonants:",number_of_letters - number_of_vowels)

with open(r'chapter1.txt','r') as file:
        for i in range(3):
            next(file)
        text = file.read()
        words = text.split()
        longest_three = sorted(words,key=len,reverse=True)
        longest_three = longest_three[:3]
        word_counts = Counter(words)
        top_five = word_counts.most_common(5)
        print("Top 5 words:")
        for word in top_five:
            print('"'+word[0]+'"', "appeared", word[1], "times")
        print("Top 3 Longest Words:")
        for word in longest_three:
            print('"'+word+'"')
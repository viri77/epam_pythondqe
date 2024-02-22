
import re

my_string = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

my_string1 = my_string.lower()#lower case
my_string2 = my_string1.replace(' iz ',' is ')#replace  standalone iz



#calculate whitespaces
symbol_counts = 0
for i in my_string2:
    if i.isspace():
        symbol_counts += 1
# print(symbol_counts)


sentences = re.split(r'(?<=[.!?])', my_string2)

# last word of every sentences
last_words = []
for sentence in sentences:
    words = re.findall(r'\b\w+\b', sentence)
    if words:
        last_word = words[-1]
        last_words.append(last_word)


word_after = 'paragraph.'
insert_index = my_string2.lower().find('paragraph')
sent_last_word = ' '.join(last_words)  #ready sentence
sentence_before_insert = my_string2[:insert_index+len(word_after)]#where to insert new sentence
sentence_after_insert = my_string2[insert_index+len(word_after):]#where continue the rest of the text after inserting new sentence
print(f"{sentence_before_insert}  {sent_last_word}. {sentence_after_insert}")

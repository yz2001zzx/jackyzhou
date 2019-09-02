#!/usr/bin/python


# Text Content Copied:

murder_note = "You may call me heartless, a killer, a monster, a murderer, but I'm still NOTHING compared to the villian that Jay was. This whole contest was a sham, an elaborate plot to shame the contestants and feed Jay's massive, massive ego. SURE you think you know him! You've seen him smiling for the cameras, laughing, joking, telling stories, waving his money around like a prop but off camera he was a sinister beast, a cruel cruel taskmaster, he treated all of us like slaves, like cattle, like animals! Do you remember Lindsay, she was the first to go, he called her such horrible things that she cried all night, keeping up all up, crying, crying, and more crying, he broke her with his words. I miss my former cast members, all of them very much. And we had to live with him, live in his home, live in his power, deal with his crazy demands. AND FOR WHAT! DID YOU KNOW THAT THE PRIZE ISN'T REAL? He never intended to marry one of us! The carrot on the stick was gone, all that was left was stick, he told us last night that we were all a terrible terrible disappointment and none of us would ever amount to anything, and that regardless of who won the contest he would never speak to any of us again! It's definitely the things like this you can feel in your gut how wrong he is! Well I showed him, he got what he deserved all right, I showed him, I showed him the person I am! I wasn't going to be pushed around any longer, and I wasn't going to let him go on pretending that he was some saint when all he was was a sick sick twisted man who deserved every bit of what he got. The fans need to know, Jay Stacksby is a vile amalgamation of all things evil and bad and the world is a better place without him."

lily_trebuchet_intro = "Hi, I'm Lily Trebuchet from East Egg, Long Island. I love cats, hiking, and curling up under a warm blanket with a book. So they gave this little questionnaire to use for our bios so lets get started. What are some of my least favorite household chores? Dishes, oh yes it's definitely the dishes, I just hate doing them, don't you? Who is your favorite actor and why? Hmm, that's a hard one, but I think recently I'll have to go with Michael B. Jordan, every bit of that man is handsome, HANDSOME! Do you remember seeing him shirtless? I can't believe what he does for the cameras! Okay okay next question, what is your perfect date? Well it starts with a nice dinner at a delicious but small restaurant, you know like one of those places where the owner is in the back and comes out to talk to you and ask you how your meal was. My favorite form of art? Another hard one, but I think I'll have to go with music, music you can feel in your whole body and it is electrifying and best of all, you can dance to it! Okay final question, let's see, What are three things you cannot live without? Well first off, my beautiful, beautiful cat Jerry, he is my heart and spirit animal. Second is pasta, definitely pasta, and the third I think is my family, I love all of them very much and they support me in everything I do. I know Jay Stacksby is a handsome man and all of us want to be the first to walk down the aisle with him, but I think he might truly be the one for me. Okay that's it for the bio, I hope you have fun watching the show!"

myrtle_beech_intro = "Salutations. My name? Myrtle. Myrtle Beech. I am a woman of simple tastes. I enjoy reading, thinking, and doing my taxes. I entered this competition because I want a serious relationship. I want a commitment. The last man I dated was too whimsical. He wanted to go on dates that had no plan. No end goal. Sometimes we would just end up wandering the streets after dinner. He called it a ""walk"". A ""walk"" with no destination. Can you imagine? I like every action I take to have a measurable effect. When I see a movie, I like to walk away with insights that I did not have before. When I take a bike ride, there better be a worthy destination at the end of the bike path. Jay seems frivolous at times. This worries me. However, it is my staunch belief that one does not make and keep money without having a modicum of discipline. As such, I am hopeful. I will now list three things I cannot live without. Water. Emery boards. Dogs. Thank you for the opportunity to introduce myself. I look forward to the competition." 

gregg_t_fishy_intro = "A good day to you all, I am Gregg T Fishy, of the Fishy Enterprise fortune. I am 37 years young. An adventurous spirit and I've never lost my sense of childlike wonder. I do love to be in the backyard gardening and I have the most extraordinary time when I'm fishing. Fishing for what, you might ask? Why, fishing for compliments of course! I have a stunning pair of radiant blue eyes. They will pierce the soul of anyone who dare gaze upon my countenance. I quite enjoy going on long jaunts through garden paths and short walks through greenhouses. I hope that Jay will be as absolutely interesting as he appears on the television. I find that he has some of the most curious tastes in style and humor. When I'm out and about I quite enjoy hearing tales that instill in my heart of hearts the fascination that beguiles my every day life. Every fiber of my being scintillates and vascillates with extreme pleasure during one of these charming anecdotes and significantly pleases my beautiful personage. I cannot wait to enjoy being on A Brand New Jay. It certainly seems like a grand time to explore life and love."


#Write a function get_average_sentence_length that takes some text as an argument. This function should return the average number of words in a sentence in the text.

def get_average_sentence_length(text):
	
	text_modified = text.replace("!",".").replace("?",".")
	text_splitted = text_modified.split(".")
	
	
	total_length = 0
	
	for sentence in text_splitted:
		
		new_sentence = sentence.replace(","," ").replace("'"," ")
		
		sentense_splitted = new_sentence.split()
		
		total_length += len(sentense_splitted)
	
	average_length = total_length/(len(text_splitted))
	
	return average_length

# Function for Text preparation

def prepare_text(text):
	
	text_lowercase = text.lower()
	
	text_lower_mod = text_lowercase.replace(","," ").replace("."," ").replace("?"," ").replace("?", " ").replace("!", " ").replace("'"," ")
	
	splitted_text_lower_mod = text_lower_mod.split()
	
	return splitted_text_lower_mod

# Build a frequency table

def build_frequency_table(corpus):
	
	table = {}
	
	for word in corpus:
		
		if word in table:
			
			table[word] += 1
		
		if word not in table:
			
			table[word] = 1
	
	return table

# n-gram func :
	
def ngram_creator(text_list):
		
	new_list = []
		
	for i in range(0,len(text_list)-1):
			
		temp_entry = text_list[i] + " " + text_list[i+1]
			
		new_list.append(temp_entry)
		
	return new_list


# frequency comparison function

def frequency_comparison(table1, table2):
	
	mutual_appearence = 0
	
	appearences = 0
	
	for key1 in table1.keys():
		
		for key2 in table2.keys(): 
			
			if key1 == key2:
				
				if table1[key1] < table2[key2]:
					
					mutual_appearence += table1[key1]
					
					appearences += table2[key2]
					
				if table1[key1] >= table2[key2]:
					
					mutual_appearence += table2[key2]
					
					appearences += table1[key1]
					
			if key1 not in table2.keys():
				
				appearences += table1[key1]
	
	comparison_score = mutual_appearence/appearences
	
	return comparison_score

# Comparing Average Sentence Length:

def percent_difference(sample1,sample2):
	
	text1 = sample1.raw_text
	
	text2 = sample2.raw_text
		
	percentage_diff = abs(sample1.average_sentence_length - sample2.average_sentence_length)/((sample1.average_sentence_length + sample2.average_sentence_length)/2)
	
	return percentage_diff

# Find the Similarity 

def find_text_similarity(sample1,sample2):
	
	text1 = sample1.raw_text
	
	text2 = sample2.raw_text
		
	sentence_length_difference = percent_difference(sample1, sample2)
	
	sentence_length_similarity = abs(1-sentence_length_difference)
	
	word_count_similarity = frequency_comparison(sample1.word_count_frequency, sample2.word_count_frequency)
	
	ngram_similarity = frequency_comparison(sample1.ngram_frequency, sample2.ngram_frequency)
	
	total_similarity = (sentence_length_similarity + word_count_similarity + ngram_similarity)/3

# Round the results to 3 decimal places for displaying cleaner results

	return total_similarity
	


#Creating The Definition for Our Model
#Now that we have a metric we want to save and data that is coupled with that metric, it might be time to create our data type. Let's define a class called TextSample with a constructor. The constructor should take two arguments: text and author. text should be saved as self.raw_text. Call get_average_sentence_length with the raw text and save it to self.average_sentence_length. You should save the author of the text as self.author.

#Additionally, define a string representation for the model. If you print a TextSample it should render:

#The author's name
#The average sentence length
#This will be your main class for the problem at hand. All later instruction to update TextSample should be done in the code block below. After updating TextSample, click on the Cell option in the Jupyter Notebook main menu above, then click Run All to rerun the cells from top to bottom. If you need to restart your Jupyter Notebook either run the cells below first or move the TextSample class definition & instantiation cells to the bottom.

class TextSample:
	
	def __init__(self, text, author):
		
		self.raw_text = text
		
		self.author = author
		
		self.average_sentence_length = get_average_sentence_length(text)
		
		self.prepared_text = prepare_text(text)
		
		self.word_count_frequency = build_frequency_table(prepare_text(text))
		
		self.ngram_frequency = build_frequency_table(ngram_creator(prepare_text(text)))
	
	def __repr__(self):
		
		return str(self.raw_text)


		
murderer_sample = TextSample(murder_note, "murder" )

print(murderer_sample)

lily_sample = TextSample(lily_trebuchet_intro, "Lily Trebuchet")

print(lily_sample)

myrtle_sample = TextSample(myrtle_beech_intro, "Myrtle Beech")

print(myrtle_sample)

gregg_sample = TextSample(gregg_t_fishy_intro, "Gregg T Fishy")

print(gregg_sample)


# -------------------For Test only--------------------------

#print(murderer_sample.raw_text)

#print(murderer_sample.prepared_text)

#print(murderer_sample.average_sentence_length)

#print(murderer_sample.word_count_frequency)

#print(murderer_sample.ngram_frequency)

# ------------------Test End---------------------------------


# Print out the results:


print(str(lily_sample.author) + "'s similarity score to the murder letter is " + str(find_text_similarity(murderer_sample, lily_sample)))
print(str(myrtle_sample.author) + "'s similarity score to the murder letter is " + str(find_text_similarity(murderer_sample, myrtle_sample)))
print(str(gregg_sample.author) + "'s similarity score to the murder letter is " + str(find_text_similarity(murderer_sample, gregg_sample)))







	
from os import listdir
from os.path import isfile, join, getsize
from collections import defaultdict
from collections import Counter
from os import getcwd
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn


def main():
	curDir = getcwd()
	filename = curDir+'/all_clean_data.csv'

	male_male_sentiment = []
	male_male_counts = Counter()

	male_female_sentiment = []
	male_female_counts = Counter()
	
	female_male_sentiment = []
	female_male_counts = Counter()
	
	female_female_sentiment = []
	female_female_counts = Counter()


	family_male_male_sentiment = []
	family_male_male_counts = Counter()

	family_male_female_sentiment = []
	family_male_female_counts = Counter()
	
	family_female_male_sentiment = []
	family_female_male_counts = Counter()
	
	family_female_female_sentiment = []
	family_female_female_counts = Counter()

	total_sentiment = defaultdict(lambda : 0)
	total_counts = Counter()

	temp_counter = 0
	with open(filename, 'r') as f:
		for line in f:
			# print line
			if temp_counter % 1000 == 0: print 'finished reading ' + str(temp_counter)
			split = line.split(',')
			word = split[4].lower()
			# print word
			synsets = swn.senti_synsets(word)

			if synsets:
				# print 'reached here'
				total_pos = 0
				total_neg = 0
				non_zero_synsets = 0
				for syns in synsets:
					if syns.pos_score() or syns.neg_score(): 
						non_zero_synsets += 1
					total_pos += syns.pos_score()
					total_neg -= syns.neg_score()

				total = (total_pos + total_neg)
				if total: 
					total = total/non_zero_synsets
					if split[6][0] == '1':
						if split[1] == 'male':
							if split[3] == 'female':
								family_male_female_sentiment.append(total)
								family_male_female_counts[word] += 1
							else:
								family_male_male_sentiment.append(total)
								family_male_male_counts[word] += 1
						else:
							if split[3] == 'female':
								family_female_female_sentiment.append(total)
								family_female_female_counts[word] += 1
							else:
								family_female_male_sentiment.append(total)
								family_female_male_counts[word] += 1
					else:
						# print "in non-family zone"
						if split[1] == 'male':
							if split[3] == 'female':
								male_female_sentiment.append(total)
								male_female_counts[word] += 1
							else:
								male_male_sentiment.append(total)
								male_male_counts[word] += 1
						else:
							if split[3] == 'female':
								female_female_sentiment.append(total)
								female_female_counts[word] += 1
							else:
								female_male_sentiment.append(total)
								female_male_counts[word] += 1
			temp_counter += 1

	f.close()

	print sum(female_male_counts.values())
	print sum(female_female_counts.values())
	print sum(male_male_counts.values())
	print sum(female_female_counts.values())
	print sum(family_female_male_counts.values())
	print sum(family_female_female_counts.values())
	print sum(family_male_male_counts.values())
	print sum(family_female_female_counts.values())

	with open(curDir+"/results/male_female_data.txt", 'w') as f:
		average = 'male_female sentiment average: ' + str(sum(male_female_sentiment)/len(male_female_sentiment))
		total_words = 'male_female total number of words: ' + str(sum(male_female_counts.values()))
		f.write(average + '\n')
		f.write(total_words + '\n')
		f.write('male_female_sentiments_csv\n')
		for syn in male_female_sentiment:
			f.write(str(syn)+ '\n')
	f.close()

	with open(curDir+"/results/male_male_data.txt", 'w') as f:
		average = 'male_male sentiment average: ' + str(float(sum(male_male_sentiment))/len(male_male_sentiment))
		total_words = 'male_male total number of words: ' + str(sum(male_male_counts.values()))
		f.write(average + '\n')
		f.write(total_words + '\n')
		f.write('male_male_sentiments_csv\n')
		for syn in male_male_sentiment:
			f.write(str(syn)+ '\n')
	f.close()



	with open(curDir+"/results/female_female_data.txt", 'w') as f:
		average = 'female_female sentiment average: ' + str(sum(female_female_sentiment)/len(female_female_sentiment))
		total_words = 'female_female total number of words: ' + str(sum(female_female_counts.values()))
		f.write(average + '\n')
		f.write(total_words + '\n')
		f.write('female_female_sentiments_csv\n')
		for syn in female_female_sentiment:
			f.write(str(syn)+ '\n')
	f.close()

	with open(curDir+'/results/female_male_data.txt', 'w') as f:
		average = 'female_male sentiment average: ' + str(sum(female_male_sentiment)/len(female_male_sentiment))
		total_words = 'female_male total number of words: ' + str(sum(female_male_counts.values()))
		f.write(average + '\n')
		f.write(total_words + '\n')
		f.write('female_male_sentiments_csv\n')
		for syn in female_male_sentiment:
			f.write(str(syn)+ '\n')
	f.close()

	with open(curDir+"/results/family_male_male_data.txt", 'w') as f:
		average = 'family_male_male sentiment average: ' + str(sum(family_male_male_sentiment)/len(family_male_male_sentiment))
		total_words = 'family_male_male total number of words: ' + str(sum(family_male_male_counts.values()))
		f.write(average + '\n')
		f.write(total_words + '\n')
		f.write('family_male_male_sentiments_csv\n')
		for syn in family_male_male_sentiment:
			f.write(str(syn)+ '\n')
	f.close()

	with open(curDir+"/results/family_male_female_data.txt", 'w') as f:
		average = 'family_male_female sentiment average: ' + str(sum(family_male_female_sentiment)/len(family_male_female_sentiment))
		total_words = 'family_male_female total number of words: ' + str(sum(family_male_female_counts.values()))
		f.write(average + '\n')
		f.write(total_words + '\n')
		f.write('family_male_female_sentiments_csv\n')
		for syn in family_male_female_sentiment:
			f.write(str(syn)+ '\n')
	f.close()

	with open(curDir+"/results/family_female_female_data.txt", 'w') as f:
		average = 'family_female_female sentiment average: ' + str(sum(family_female_female_sentiment)/len(family_female_female_sentiment))
		total_words = 'family_female_female total number of words: ' + str(sum(family_female_female_counts.values()))
		f.write(average + '\n')
		f.write(total_words + '\n')
		f.write('family_female_female_sentiments_csv\n')
		for syn in family_female_female_sentiment:
			f.write(str(syn)+ '\n')
	f.close()

	with open(curDir+"/results/family_female_male_data.txt", 'w') as f:
		average = 'family_female_male sentiment average: ' + str(sum(family_female_male_sentiment)/len(family_female_male_sentiment))
		total_words = 'family_female_male total number of words: ' + str(sum(family_female_male_counts.values()))
		f.write(average + '\n')
		f.write(total_words + '\n')
		f.write('family_female_male_sentiments_csv\n')
		for syn in family_female_male_sentiment:
			f.write(str(syn)+ '\n')
	f.close()





if __name__=='__main__':
	main()

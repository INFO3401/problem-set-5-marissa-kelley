################################################################################
# PART #1
################################################################################
#I worked with Jacob Paul, Hannah Weber, Taylor Lawrence, Amy Zhai, Steven Rothaus 

def countWordsUnstructured(filename):
    wordcount = {} #initialize a word count dictionary
    file = open(filename) #open the file
    for word in file.read().split(): #split out into words and count the words
        for mark in string.punctuation:
            word = word.replace(mark, "")
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    print (wordcount) #print the word count dictionary 
         
    # This function should count the words in an unstructured text document
    # Inputs: A file name (string)
    # Outputs: A dictionary with the counts for each word
    # +1 bonus point for removing punctuation from the wordcounts
import string

#In class October 1st work
#def countWordsUndstructured(filename):
    #initalize a word count dictionary 
    #wordCounts = {} 
   
    #open the file & read it 
    #datafile = open(filename).read()
    
    #split out into words 
    #data = datafile.split() 
   
    #Count the words
    #for word in data: 
        #for mark in string.punctuation:
            #word = word.replace(mark, "")
        #if word in wordCounts:
            #wordCounts[word] = wordCounts[word] + 1
        #else: 
            #wordCounts[word] = 1
    
    #return the word count dictionary
    #return wordCounts 
################################################################################
# PART 2
################################################################################
#I worked with Hannah Weber, Taylor Lawrence

#import csv
import csv

def generateSimpleCSV(targetfile, wordCounts):  
    wordCounts = []
    #open the csv 
    with open (targetfile, 'w') as csv_file:
        #write to the csv using commas as a seperator 
        writer = csv.writer(csv_file)
    #make a header noting Word, Count
    writer.writerow(['Word', 'Count'])
    
    #make word count dictionary to a csv
    for key, value in wordCounts.items():
        writer.writerow([key,value[0]]) #SOMETHING IS FUNKY 
   

 #txt_file = r"state-of-the-union-corpus-1989-2017/Bush_1989.txt"
    
   #in_txt = csv.reader(open(txt_file, "rb"), delimerter = '\t')
    #out_csv = csv.writer(open(csv_file, 'wb'))
    
    #out_csv.writewrows(in_txt)
    #Create a header for the CSV 
    
generateSimpleCSV('PleaseWork', countWordsUnstructured('state-of-the-union-corpus-1989-2017/Bush_1989.txt'))

    # This function should transform a dictionary containing word counts to a
    # CSV file. The first row of the CSV should be a header noting: 
    # Word, Count
    # Inputs: A word count list and a name for the target file
    # Outputs: A new CSV file named targetfile containing the wordcount data
    
# Test your part 2 code below
    
################################################################################
# PART 3
################################################################################
#def countWordsMany(directory): 
    # This function should create a dictionary of word count dictionaries
    # The dictionary should have one dictionary per file in the directory
    # Each entry in the dictionary should be a word count dictionary
    # Inputs: A directory containing a set of text files
    # Outputs: A dictionary containing a word count dictionary for each
    #          text file in the directory
    
# Test your part 3 code below

################################################################################
# PART 4
################################################################################
#def generateDirectoryCSV(wordCounts, targetfile): 
    # This function should create a CSV containing the word counts generated in
    # part 3 with the header: 
    # Filename, Word, Count
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: A CSV file named targetfile containing the word count data
    
# Test your part 4 code below
    
################################################################################
# PART 5
################################################################################
#def generateJSONFile(wordCounts, targetfile): 
    # This function should create an containing the word counts generated in
    # part 3. Architect your JSON file such that the hierarchy will allow
    # the user to quickly navigate and compare word counts between files. 
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: An JSON file named targetfile containing the word count data
    
# Test your part 5 code below

################################################################################
# PART 6
################################################################################
#def searchCSV(csvfile, word): 
    # This function should search a CSV file from part 4 and find the filename
    # with the largest count of a specified word
    # Inputs: A CSV file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    
#def searchJSON(JSONfile, word): 
    # This function should search a JSON file from part 5 and find the filename
    # with the largest count of a specified word
    # Inputs: An JSON file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    
# Test your part 6 code to find which file has the highest count of a given word

# +1 bonus point for figuring out how many datapoints you had to process to 
# compute this value

countWordsUnstructured('state-of-the-union-corpus-1989-2017/Bush_1989.txt')


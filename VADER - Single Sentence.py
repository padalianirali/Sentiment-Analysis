"""
Performing sentiment analysis using VADER

"""

#import SentimentIntensityAnalyzer class from vaderSentiment.vaderSentiment module
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#function: To print sentiments of input sentences
def sentiment_scores(sentence):
    #create an object of SentimentIntensityAnalyzer class
    sia_obj = SentimentIntensityAnalyzer()
    #use method polarity_scores of SentimentIntensityAnalyzer class to get sentiment dictionary as output
    #sentiment dictionary contains pos, neg, neu and compound scores for each sentence given as input
    sentiment_dict = sia_obj.polarity_scores(sentence)
    
    print("Dictionary: ",sentiment_dict)
    print("Sentence is :",sentiment_dict['pos']*100," positive.")
    print("Sentence is :",sentiment_dict['neg']*100," negative.")
    print("Sentence is :",sentiment_dict['neu']*100," neutral.")
    
    print("Sentence overall rated as:",end=' ')
    if sentiment_dict['compound']>=0.05:
        print("Positive")
    elif sentiment_dict['compound']<= -0.05:
        print("Negative")
    else:
        print("Neutral")

#main method:
if __name__ == "__main__":
    
    sentence1 = "My name is Nirali."
    print("Statement 1: "+sentence1)
    sentiment_scores(sentence1)
    print("\n")
    
    sentence2 = "I like pizza."
    print("Statement 2: "+sentence2)
    sentiment_scores(sentence2)
    print("\n")

    sentence3 = "I hate action movies."
    print("Statement 3: "+sentence3)
    sentiment_scores(sentence3)   
    print("\n")



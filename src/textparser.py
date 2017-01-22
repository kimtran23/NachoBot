import textrazor
import tweepySetup
import string
import ypQuery

textrazor.api_key = "d1103f73c05ca5009594951423c82b86c45df568afebc6df42f20769"

sentenceList = tweepySetup.tweetMsg()
print(sentenceList)
exclude = set(string.punctuation)
for s in sentenceList:
    sentence = ''.join(ch for ch in s if ch not in exclude)
    if len(sentence) > 1:
        responselist = sentence.split()

        wordlist = []
        client = textrazor.TextRazor(extractors=["words"])
        response = client.analyze(sentence)
        for word in response.words():
            wordlist.append(word.part_of_speech)

        flag = []
        specialword = []

        for idx, word in enumerate(wordlist):
            if word == "VB" or word == "VBP" or word == "TO" or word == "DT" or word == "JJ" or word == "JJS":
                flag.append(idx)

        lastind = 0

        if len(flag) != 0:
            for i in flag:
                if wordlist[i + 1] == "NN" or wordlist[i + 1] == "NNS" or wordlist[i + 1] == "NNP" or wordlist[i + 1] == "NNPS":
                    specialword.append(responselist[i + 1])
                    lastind = i
                    break

            try:
                if wordlist[lastind + 2] == "NN" or wordlist[lastind + 2] == "NNS" or wordlist[lastind + 2] == "NNP" or wordlist[lastind + 2] == "NNPS":
                    specialword.append(responselist[lastind + 2])
            except IndexError:
                pass
    tweepySetup.replyTo(ypQuery.getResults(what=','.join(specialword)))

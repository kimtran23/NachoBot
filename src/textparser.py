import textrazor
import tweepySetup
import string

textrazor.api_key = "206536a24ac40e9b546a305489d9c83837c9200a269919d03db61b09"

sentenceList = tweepySetup.tweetMsg()
exclude = set(string.punctuation)
for s in sentenceList:
    sentence = ''.join(ch for ch in s if ch not in exclude)
    responselist = sentence.split()
    # output = ""
    # lastWord = responselist[-1]
    # for char in lastWord:
    #     if "." in char:
    #         tmp = " "+"."
    #         output = output + tmp
    #     elif "?" in char:
    #         tmp = " "+"?"
    #         output = output + tmp
    #     elif "!" in char:
    #         tmp = " "+"!"
    #         output = output + tmp
    #     else:
    #         output = output + char
    # output = output.split()
    # responselist[-1] = output[0]
    # responselist.append(output[-1])

    wordlist = []
    client = textrazor.TextRazor(extractors=["words"])
    response = client.analyze(sentence)
    for word in response.words():
        wordlist.append(word.part_of_speech)


    flag = []
    specialword = []

    for idx, word in enumerate(wordlist):
        if word == "VB" or word=="VBP" or word=="TO" or word=="DT" or word=="JJ" or word=="JJS":
            flag.append(idx)

    lastind = 0
    print(len(flag))
    print(len(responselist))
    if len(flag)!=0:
        for i in flag:
             if wordlist[i+1] == "NN" or wordlist[i+1]=="NNS" or wordlist[i+1]=="NNP" or wordlist[i+1]=="NNPS":
                #  print(i)
                 specialword.append(responselist[i+1])
                 lastind = i
                 break

        try:
            if wordlist[lastind+2]=="NN" or wordlist[lastind+2]=="NNS" or wordlist[lastind+2]=="NNP" or wordlist[lastind+2]=="NNPS":
                specialword.append(responselist[lastind+2])
        except IndexError:
            pass
    print (sentence)
    print(specialword)

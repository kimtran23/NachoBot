import textrazor

textrazor.api_key = "206536a24ac40e9b546a305489d9c83837c9200a269919d03db61b09"

sentence = "Where can I get Louis Vuitton shoes."
responselist = sentence.split()
output = ""
r = responselist[-1]
for c in r:
    if "." in c:
        tmp = " "+"."
        output = output + tmp
    elif "?" in c:
        tmp = " "+"?"
        output = output + tmp
    elif "!" in c:
        tmp = " "+"!"
        output = output + tmp
    else:
        output = output + c

output = output.split()
responselist[-1] = output[0]
responselist.append(output[-1])

client = textrazor.TextRazor(extractors=["words"])
response = client.analyze(sentence)

wordlist = list()
print (responselist)
for word in response.words():
    wordlist.append(word.part_of_speech)
flag = list()
print(wordlist)

for idx, word in enumerate(wordlist):
    if word == "VB" or word=="VBP" or word=="TO" or word=="DT" or word=="JJ" or word=="JJS":
        flag.append(idx)
specialword = list()
lastind = 0
for i in flag:
     if wordlist[i+1] == "NN" or wordlist[i+1]=="NNS" or wordlist[i+1]=="NNP" or wordlist[i+1]=="NNPS":
         specialword.append(responselist[i+1])
         lastind = i
         break

try:
    if wordlist[lastind+2]=="NN" or wordlist[lastind+2]=="NNS" or wordlist[lastind+2]=="NNP" or wordlist[lastind+2]=="NNPS":
        specialword.append(responselist[lastind+2])
except IndexError:
    pass

print(specialword)

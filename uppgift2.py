# Programmeringsteknik webbkurs KTH inlämningsuppgift 2.
# <Andreas Larsson>
# <2013-07-10>
# <Programmet kommer att skapa en dikt av fyra meningar som skrivs in>

def split_data (data):#Delar upp indatan och returnerar en lista med den uppdelade indatan
    indata_split = data.split()
    return indata_split

def join_list (sentence):#Slår ihop inparametern och returnerar denna
    joined_str = " ".join(sentence)
    return joined_str
    
def print_text():

    sentence = splt_sentences[0]#Tilldelar sentence den uppdelade listan i splt_sentence
    print(join_list(sentence[0:4]).upper())#Sätter ihop en mening med de givna vilkoren
    print("")
    print(join_list(sentence[0:4]))
    print(join_list(sentence[4:len(sentence)]))
    print(join_list(sentence[0:4]))
    sentence = splt_sentences[1]
    print(join_list(sentence))
    sentence = splt_sentences[2]
    print(join_list(sentence))
    sentence = splt_sentences[3]
    print(join_list(sentence))
    sentence = splt_sentences[0]
    print(join_list(sentence[0:4]))

indata = 4*[None]
i = 0
while i < 4:
    indata[i] = input("Skriv in mening " + str(i + 1))#Tar all indata från användaren och sparar dessa i en lista
    i += 1
i = 0
splt_sentences = 4*[None]
for data in indata:
    splt_sentences[i] = split_data(data)#Sparar de uppdelade meningarna i en lista
    i +=1

print_text()#Skriver ut texten på skärmen

#!/usr/bin/env python3
Kasus = ["N", "G", "D", "A"]
Genera = ["m", "n", "f", "pl"]
Art = ["o", "u", "b"]
kasus_name = {"N": "Nominativ", "G": "Genitiv", "D": "Dativ ", "A":\
"Akkusativ"}
genera_name = {"m": "Maskulin", "n": "Neutrum", "f": "Feminin", "pl":\
"Plural"}
art_name = {"o": "Ohne", "u": "Unbstmm", "b": "Bstmm"}
best_art = {"m": {"N": "der", "G": "des", "D": "dem", "A": "den"},\
            "n": {"N": "das", "G": "des", "D": "dem", "A": "das"},\
            "f": {"N": "die", "G": "der", "D": "der", "A": "die"},\
            "pl":{"N": "die", "G": "der", "D": "den", "A": "die"}}
unbest_art = {"m": {"N": "ein", "G": "eines", "D": "einem", "A": "einen"},\
            "n": {"N": "ein", "G": "eines", "D": "einem", "A": "ein"},\
            "f": {"N": "eine", "G": "einer", "D": "einer", "A": "eine"}}
Adj_end = {"o":\
  {"m": {"N": "er", "G": "en", "D": "em", "A": "en"},\
   "n": {"N": "es", "G": "en", "D": "em", "A": "es"},\
   "f": {"N": "e", "G": "er", "D": "er", "A": "e"},\
   "pl":{"N": "e", "G": "er", "D": "en", "A": "e"}},\
           "u":\
  {"m": {"N": "er", "G": "en", "D": "en", "A": "en"},\
   "n": {"N": "es", "G": "en", "D": "en", "A": "es"},\
   "f": {"N": "e", "G": "en", "D": "en", "A": "e"}},\
           "b":\
  {"m": {"N": "e", "G": "en", "D": "en", "A": "en"},\
   "n": {"N": "e", "G": "en", "D": "en", "A": "e"},\
   "f": {"N": "e", "G": "en", "D": "en", "A": "e"},\
   "pl":{"N": "en","G": "en", "D": "en", "A": "en"}}}
empty={"N": "", "G": "", "D": "", "A": ""}
empty2 = {"m": empty, "n": empty, "f": empty, "pl": empty}
art_table = {"o": empty2, "u": unbest_art, "b": best_art}
"""
print "Unbst - Bst"
for g in Genera:
  print "\t\t",genera_name [g]
  for k in Kasus:
    if g != "pl":
      print kasus_name[k],":\t",unbest_art[g][k], "-", best_art[g][k] 
    else:
      print kasus_name[k],":\t", best_art[g][k] 
print art_name["u"], genera_name["f"], kasus_name\
["G"], Adj_end["u"]["f"]["G"]
"""
import random, os
random.seed (os.urandom(5))
art=None; genera=None; kas=None;
art=random.choice (Art)
genera=random.choice (Genera)
kas=random.choice (Kasus)
print("Enter article and corresponding ending of adjective")
print(art_name[art], "Artikel,", genera_name[genera], kasus_name[kas])
answer=input ("** ")
answer = answer.split()
correct_answer = art_table[art][genera][kas]+" "+Adj_end[art][genera][kas]
correct_answer = correct_answer.split()
if answer != correct_answer:
  print("Wrong answer, correct is: ", " ".join(correct_answer))
else:
  print("Correct.")

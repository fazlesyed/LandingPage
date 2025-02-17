import numpy as np
import pandas as pd
data = pd.DataFrame(data=pd.read_csv("C:\Users\fazle\OneDrive\Desktop\ai\data.csv.xlsx"))
concepts = np.array(data.iloc[:0:-1])
target=np.array(data.iloc[:,-1])
def learn(concepts, target): 
 specific_h = concepts[0].copy()
 print("\nInitialization of specific_h and genearal_h")
 print("\nSpecific hypothesis: ", specific_h)
 general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
 print("\nGeneric hypothesis: ",general_h)
 print()
 print("concepts:",concepts)

 for i, h in enumerate(concepts):
   if target[i] == "yes":
      for x in range(len(specific_h)): 
        if h[x]!= specific_h[x]: 
           specific_h[x] ='?' 
           general_h[x][x] ='?'
 
   if target[i] == "no": 
      for x in range(len(specific_h)): 
        if h[x]!= specific_h[x]: 
           general_h[x][x] = specific_h[x] 
        else: 
           general_h[x][x] = '?'
 
 print("\n Steps for Candidate Algorithm:",i+1) 
 print("Specific Hypothesis:",i+1)
 print(specific_h)
 print("General Hypothesis:",i+1)
 print(general_h)

 indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']] 
 print("\n Indices:",indices)
 for i in indices:
   general_h.remove(['?','?','?','?','?','?'])
 return specific_h,general_h
 
s_final, g_final = learn(concepts, target)

print("Final Specific_h: ", s_final)
print("Final General_h: ", g_final)

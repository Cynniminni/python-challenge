#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


poll_data=os.path.join('Resources','election_data.csv')


# In[3]:


with open(poll_data, 'r') as csvfile:
    poll_csv = csv.reader(csvfile, delimiter=',')

    NoOfRows=[]

    for row in poll_csv:

        NoOfRows.append(row)
    header=NoOfRows.pop(0)


# In[37]:





# In[35]:


Candidate_Dict = {}
Candidate_List=[]
Candidate_Votes={}
for row in NoOfRows:
    if row[2] not in Candidate_List:
        Candidate_List.append(row[2])



Votes0 = 0
Votes1 = 0
Votes2 = 0
Votes3 = 0

for row in NoOfRows:
    if row[2] == Candidate_List[0]:
        Votes0 +=1
    if row[2] == Candidate_List[1]:
        Votes1 +=1
    if row[2] == Candidate_List[2]:
        Votes2 +=1
    if row[2] == Candidate_List[3]:
        Votes3 +=1
    #calculate vote percentage for each candidate
    #candidate_list[0]=(float(votes0)/float(len(NoOfRows))100


# In[52]:


Per1 = (float(Votes0)/float(len(NoOfRows)))*100
Per2 = (float(Votes1)/float(len(NoOfRows)))*100
Per3 = (float(Votes2)/float(len(NoOfRows)))*100
Per4 = (float(Votes3)/float(len(NoOfRows)))*100


# Candidate_List[0]> key
# Votes0 will be the value for Candidate_List[0]

# In[55]:


winner = max(Votes0,Votes1,Votes2,Votes3)

if winner == Votes0:
    winner = Candidate_List[0]
elif winner == Votes1:
    winner=Candidate_List[1]
elif winner == Votes2:
    winner=Candidate_List[2]
elif winner == Votes3:
    winner=Candidate_List[3]


# In[75]:


print("Election Results")
print("-----------------------------")
print("Total Votes: "+ str(len(NoOfRows)))
print("-----------------------------")
print(f"{Candidate_List[0]}: {round(Per1,3)}% ({Votes0})")
print(f"{Candidate_List[1]}: {round(Per2,3)}% ({Votes1})")
print(f"{Candidate_List[2]}: {round(Per3,3)}% ({Votes2})")
print(f"{Candidate_List[3]}: {round(Per1,3)}% ({Votes3})")
print("-----------------------------")
print(f"Winner: {winner}")
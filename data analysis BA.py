# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:42:25 2023

@author: Acer
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/Acer/Downloads/Description_only_750.csv")

words = list(df['Description'])
lowercase_words = [x.lower() for x in words]

df = pd.read_csv("C:/Users/Acer/Downloads/archive/linkedin-jobs-usa.csv") 
criteria = list(df['criteria'])
desc = list(df['description'])
lowercase_desc = [x.lower() for x in desc]   

lowercase_crit = [x.lower() for x in criteria]   

n = len(words)
m = len(criteria)

skills_counts = {
    "python_count": 0,
    "r_count": 0,
    "sql_count": 0,
    "leader_count": 0,
    "communication_count": 0,
    "ps_count": 0,
    "creative_count": 0,
    "excel_count": 0,
    "java_count" : 0  ,
    "hard_count" : 0,
    "soft_count" : 0,    
    "skill_count" : 0,  
    "total_count" : len(words)+ len(criteria)
}

count = [0 for i in range(n+m)]
hard_count = [0 for i in range(n+m)]
total_count = [0 for i in range(n+m)]
soft_count = [0 for i in range(n+m)]
for i in range(n):
    if 'python' in words[i]:
        skills_counts["python_count"] += 1
        hard_count[i] = 1
        total_count[i] = 1
    if 'sql' in words[i]:
        skills_counts["sql_count"] += 1      
        hard_count[i] = 1
        total_count[i] = 1
    if 'leader' in words[i]:
        skills_counts["leader_count"] += 1
        soft_count[i] = 1
        total_count[i] = 1
    if 'communicat' in words[i]:
        skills_counts["communication_count"] += 1
        soft_count[i] = 1
        total_count[i] = 1
    if 'problem solv' in words[i] or ('solv' in words[i] and 'problem' in words[i]) or 'problem-solv' in words[i]:
        skills_counts["ps_count"] += 1
        soft_count[i] = 1
        total_count[i] = 1
    if 'creativ' in words[i]:
        skills_counts["creative_count"] += 1
        soft_count[i] = 1
        total_count[i] = 1
    if 'excel' in words[i]:
        skills_counts["excel_count"] += 1
        hard_count[i] = 1
        total_count[i] = 1
    if 'java' in words[i]:
        skills_counts["java_count"] += 1
        hard_count[i] = 1
        total_count[i] = 1
    skills_counts["skill_count"] += total_count[i]
    skills_counts["soft_count"] += soft_count[i]
    skills_counts["hard_count"] += hard_count[i]    
        
for i in range(n): 
    if 'R ' in words[i] or 'R, ' in words[i]:
        skills_counts["r_count"] += 1
        if hard_count[i] != 1:
            skills_counts["skill_count"] += 1
            skills_counts["hard_count"] += 1
   
      
df = pd.read_csv("C:/Users/Acer/Downloads/archive/linkedin-jobs-usa.csv") 
criteria = list(df['criteria'])
desc = list(df['description'])
lowercase_desc = [x.lower() for x in desc]   


lowercase_crit = [x.lower() for x in criteria]   

for i in range(m):
    if 'python' in lowercase_crit[i] or 'python' in lowercase_desc[i]:
        skills_counts["python_count"] += 1
        hard_count[n+i] = 1
        total_count[n+i] = 1
    if 'sql' in lowercase_crit[i] or 'sql' in lowercase_desc[i]:
        skills_counts["sql_count"] += 1
        hard_count[n+i] = 1
        total_count[n+i] = 1
    if 'leader' in lowercase_crit[i] or 'leader' in lowercase_desc[i]:
        skills_counts["leader_count"] += 1
        soft_count[n+i] = 1
        total_count[n+i] = 1
    if 'communicat' in lowercase_crit[i] or 'communicat' in lowercase_desc[i]:
        skills_counts["communication_count"] += 1
        soft_count[n+i] = 1
        total_count[n+i] = 1
    if ('problem solv' in lowercase_crit[i] or ('solv' in lowercase_crit[i] and 'problem' in lowercase_crit[i]) or 'problem-solv' in lowercase_crit[i]) or ('problem solv' in lowercase_desc[i] or ('solv' in lowercase_desc[i] and 'problem' in lowercase_desc[i]) or 'problem-solv' in lowercase_desc[i]):
        skills_counts["ps_count"] += 1
        soft_count[n+i] = 1
        total_count[n+i] = 1
    if 'creativ' in lowercase_crit[i] or 'creativ' in lowercase_desc[i]:
        skills_counts["creative_count"] += 1
        soft_count[n+i] = 1
        total_count[n+i] = 1
    if 'excel' in lowercase_crit[i] or 'excel' in lowercase_desc[i]:
        skills_counts["excel_count"] += 1
        hard_count[n+i] = 1
        total_count[n+i] = 1
    if 'java' in lowercase_crit[i] or 'excel' in lowercase_desc[i]:
        skills_counts["java_count"] += 1
        hard_count[n+i] = 1
        total_count[n+i] = 1
    skills_counts["skill_count"] += total_count[n+i]
    skills_counts["soft_count"] += soft_count[n+i]
    skills_counts["hard_count"] += hard_count[n+i]

    
        
for i in range(m):
    if 'R ' in criteria[i] or 'R, ' in criteria[i] or 'R ' in desc[i] or 'R, ' in desc[i]:
        skills_counts["r_count"] += 1    
        if hard_count[n+i] != 1:
            skills_counts["skill_count"] += 1
            skills_counts["hard_count"] += 1




print(skills_counts)

skills = list(skills_counts.keys())
counts = list(skills_counts.values())
plt.figure(figsize=(10, 6))
plt.barh(skills, counts, color='lightgreen')
plt.xlabel('Count')
plt.title('Skill Counts')
plt.show()


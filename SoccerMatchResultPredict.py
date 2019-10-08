import pandas as pd

def load_dataset():
    df = pd.read_csv('Dataset.csv')
    dataset = df[['HomeTeam','AwayTeam','FTHG','FTAG','FTR']]
    return dataset

dataset = load_dataset()

MU_Home_Win = 0
LV_Away_Win = 0
Draw = 0

for team,res in zip(dataset[['HomeTeam']].values.tolist(),dataset[['FTR']].values.tolist()):
    if team[0] == 'Man United' and res[0]  == 'H':
        MU_Home_Win += 1
    elif team[0] == 'Man United' and res[0]  == 'A':
        LV_Away_Win += 1
    elif team[0] == 'Man United' and res[0]  == 'D':
       Draw += 1

chance_MU_Win = (float(MU_Home_Win) / float(MU_Home_Win + LV_Away_Win + Draw)) * 100
chance_LV_Win = (float(LV_Away_Win) / float(LV_Away_Win + MU_Home_Win + Draw)) * 100
chance_draw = (float(Draw) / float(MU_Home_Win + LV_Away_Win + Draw)) * 100

print('\n'*30)
print('Based on previous match between Manchester United and Liverpool') 
print('this is a simple match result prediction for 20th October 2019 match')
print()
print('Manchester United win the match: {}%'.format(chance_MU_Win))
print('Manchester United and Liverpool draw: {}%'.format(chance_draw))
print('Liverpool win the match: {}%'.format(chance_LV_Win))
import pandas as pd

año,mes,modulo=2011,'Febrero','Cv'
pd.read_csv(f'src\geihdanepy\sets\{año}\{mes}.csv\{modulo}.csv', sep = ';')

12*24
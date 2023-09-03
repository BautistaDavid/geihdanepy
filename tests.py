import pandas as pd

año,mes,modulo=2021,'Febrero','Ai'
pd.read_csv(f'src\geihdanepy\sets\{año}\{mes}.csv\{modulo}.csv', sep = ';').columns

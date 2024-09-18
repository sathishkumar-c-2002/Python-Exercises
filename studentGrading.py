#Dictionary 

studentScores = {"Sathish":90,
                 "Pradeep":95,
                 "Ragul":85,
                 "Ellappan":98,
                 "Nandha":74,    
                }
for i in studentScores:
    if 90>studentScores[i]<=100:
        print(f"{i}'s Grade : OutStanding.")
    if 80>studentScores[i]<=90:
        print(f"{i}'s Grade : Exceed Expectation.")
    if 70>studentScores[i]<=80:
        print(f"{i}'s Grade : Acceptable.")        
    if studentScores[i]<=70:
        print(f"{i}'s Grade : Fail.") 
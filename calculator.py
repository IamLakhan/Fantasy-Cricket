import sqlite3

data = sqlite3.connect("database.db")
datacur = data.cursor()
datacur.execute("SELECT * FROM match")
pdata = datacur.fetchall()

def calculate_points(pdata):# Calculates points
    points = 0.0
    score = pdata[1]
    try:
        strike_rate = float(pdata[1]) / float(pdata[2])
    except:
        strike_rate = 0
    fours, sixes = float(pdata[3]), float(pdata[4])

    twos = int(((score - (4 * fours) - (6 * sixes))) / 2)
    wickets = 10 * float(pdata[8])
    try:
        economy = float(pdata[7]) / (float(pdata[5]) / 6)
    except:
        economy = 0
    Fielding = float(pdata[9]) + float(pdata[10]) + float(pdata[11])

    points += (fours + (2 * sixes) + (10 * Fielding) + twos + wickets)
    if score > 100:
        points += 10
    elif score >= 50:
        points += 5 
    if strike_rate > 1:
        points += 4
    elif strike_rate >= 0.8:
        points += 2 
    if wickets >= 5:
        points += 10 
    elif wickets > 3:
        points += 5 
    if economy >= 3.5 and economy <= 4.5:
        points += 4 
    elif economy >= 2 and economy < 3.5:
        points += 7 
    elif economy < 2:
        points += 10 
    return points

player_points = {}
for p in pdata: # calculates points and stores in dictionary
    player_points[p[0]] = calculate_points(p)

print(player_points)
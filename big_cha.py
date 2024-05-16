#!/usr/bin/env python3
import requests

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

seasonId = 52760

teamIdHome = 2693
teamIdAway = 2442
# teamLocation = 1

excludeId = False

teamData = requests.get('https://www.sofascore.com/api/v1/team/{}'.format(teamIdHome), headers=headers)
team = teamData.json()
print(team['team']['name'])
print('---------------------------------')
big_chances_home = []
big_chances_home_conc = []
big_chances_missed_home = []
big_chances_missed_home_conc = []
big_chances_away = []
big_chances_away_conc = []
big_chances_missed_away = []
big_chances_missed_away_conc = []
goalsHome = []
goalsHomeConc = []
goalsAway = []
goalsAwayConc = []
xgHome = []
xgHomeConc = []
xgAway = []
xgAwayConc = []
for i in range(3):
    response = requests.get('https://www.sofascore.com/api/v1/team/{}/events/last/{}'.format(teamIdHome, i), headers=headers)
    data = response.json()
    for event in data['events']:
        try:
            if event['homeTeam']['id'] == teamIdHome and event['season']['id'] == seasonId and event['id'] != excludeId:
                # ids.append(event['id'])
                # print(event['id'])
                goalsHome.append(event['homeScore']['normaltime'])
                goalsHomeConc.append(event['awayScore']['normaltime'])
                res = requests.get('https://api.sofascore.com/api/v1/event/{}/statistics'.format(event['id']), headers=headers)
                data1 = res.json()
                for stat in data1['statistics'][0]['groups']:
                    if stat['groupName'] == 'Expected':
                        if stat['statisticsItems'][0]['name'] == 'Expected goals':
                            # print(type(stat['statisticsItems'][0]['home']))
                            temp_xg = float(stat['statisticsItems'][0]['home'])
                            temp_xg_conc = float(stat['statisticsItems'][0]['away'])
                    if stat['groupName'] == 'Shots extra':
                        if stat['statisticsItems'][0]['name'] == 'Big chances':
                            temp_big_cha = int(stat['statisticsItems'][0]['home'])
                            temp_big_cha_conc = int(stat['statisticsItems'][0]['away'])
                            # print('big chances')
                            # print('---------------------------------')
                            # print(temp_big_cha, temp_big_cha_conc)
                        if stat['statisticsItems'][1]['name'] == 'Big chances missed':
                            # print('big chances missed')
                            # print('--------------------------------')
                            temp_big_cha_miss = int(stat['statisticsItems'][1]['home'])
                            temp_big_cha_miss_conc = int(stat['statisticsItems'][1]['away'])
                            # print(temp_big_cha_miss, temp_big_cha_miss_conc)
                        break
                big_chances_home.append(temp_big_cha)
                big_chances_home_conc.append(temp_big_cha_conc)
                big_chances_missed_home.append(temp_big_cha_miss)
                big_chances_missed_home_conc.append(temp_big_cha_miss_conc)
                xgHome.append(temp_xg)
                xgHomeConc.append(temp_xg_conc)
        except (TypeError, KeyError, NameError):
            continue
big_chances_home_pg = sum(big_chances_home)/len(big_chances_home)
big_chances_made_pg = (sum(big_chances_home) - sum(big_chances_missed_home))/len(big_chances_home)
big_chances_conc_pg = sum(big_chances_home_conc)/len(big_chances_home_conc)
big_chances_conc_made_pg = (sum(big_chances_home_conc) - sum(big_chances_missed_home_conc))/len(big_chances_home_conc)
goalsScoredHome = round(sum(goalsHome) / len(goalsHome), 2)
goalsConcHome = round(sum(goalsHomeConc) / len(goalsHomeConc), 2)
print('{}: {}'.format(stat['statisticsItems'][0]['name'], round(big_chances_home_pg, 2)))
print('Big chances made(per game): {}'.format(round(big_chances_made_pg, 2)))
print('Big chances conceded: {}'.format(round(big_chances_conc_pg, 2)))
print('Big chances conceded made(per game): {}'.format(round(big_chances_conc_made_pg, 2)))
try:
    print('Expected goals: {}'.format(round(sum(xgHome) / len(xgHome), 2)))
    print('Expected goals conceded: {}'.format(round(sum(xgHomeConc) / len(xgHomeConc), 2)))
except (ZeroDivisionError):
    print('!!!Could not get xG stats!!!')
print('Goals scored: {}'.format(goalsScoredHome))
print('Goals conceded: {}'.format(goalsConcHome))
print(len(big_chances_home))
print(len(big_chances_missed_home))
# print(big_chances_home)
print('----------------------------------------')
print('----------------------------------------')

teamData = requests.get('https://www.sofascore.com/api/v1/team/{}'.format(teamIdAway), headers=headers)
team = teamData.json()
print(team['team']['name'])
print('---------------------------------')
for i in range(3):
    response = requests.get('https://www.sofascore.com/api/v1/team/{}/events/last/{}'.format(teamIdAway, i), headers=headers)
    data = response.json()
    for event in data['events']:
        try:
            if event['awayTeam']['id'] == teamIdAway and event['season']['id'] == seasonId and event['id'] != excludeId:
                # ids.append(event['id'])
                # print(event['id'])
                goalsAway.append(event['awayScore']['normaltime'])
                goalsAwayConc.append(event['homeScore']['normaltime'])
                res = requests.get('https://api.sofascore.com/api/v1/event/{}/statistics'.format(event['id']), headers=headers)
                data1 = res.json()
                for stat in data1['statistics'][0]['groups']:
                    if stat['groupName'] == 'Expected':
                        if stat['statisticsItems'][0]['name'] == 'Expected goals':
                            temp_xg = float(stat['statisticsItems'][0]['away'])
                            temp_xg_conc = float(stat['statisticsItems'][0]['home'])
                    if stat['groupName'] == 'Shots extra':
                        if stat['statisticsItems'][0]['name'] == 'Big chances':
                            temp_big_cha = int(stat['statisticsItems'][0]['away'])
                            temp_big_cha_conc = int(stat['statisticsItems'][0]['home'])
                            # print('big chances')
                            # print('---------------------------------')
                            # print(temp_big_cha, temp_big_cha_conc)
                        if stat['statisticsItems'][1]['name'] == 'Big chances missed':
                            temp_big_cha_miss = int(stat['statisticsItems'][1]['away'])
                            temp_big_cha_miss_conc = int(stat['statisticsItems'][1]['home'])
                            # print('big chances missed')
                            # print('--------------------------------')
                            # print(temp_big_cha_miss, temp_big_cha_miss_conc)
                        break
                big_chances_away.append(temp_big_cha)
                big_chances_away_conc.append(temp_big_cha_conc)
                big_chances_missed_away.append(temp_big_cha_miss)
                big_chances_missed_away_conc.append(temp_big_cha_miss_conc)
                xgAway.append(temp_xg)
                xgAwayConc.append(temp_xg_conc)
        except (TypeError, KeyError, NameError):
            continue
big_chances_away_pg = sum(big_chances_away)/len(big_chances_away)
big_chances_away_made_pg = (sum(big_chances_away) - sum(big_chances_missed_away))/len(big_chances_away)
big_chances_away_conc_pg = sum(big_chances_away_conc)/len(big_chances_away_conc)
big_chances_away_conc_made_pg = (sum(big_chances_away_conc) - sum(big_chances_missed_away_conc))/len(big_chances_away_conc)
goalsScoredAway = round(sum(goalsAway) / len(goalsAway), 2)
goalsConcAway = round(sum(goalsAwayConc) / len(goalsAwayConc), 2)
print('{}: {}'.format(stat['statisticsItems'][0]['name'], round(big_chances_away_pg, 2)))
print('Big chances made(per game): {}'.format(round(big_chances_away_made_pg, 2)))
print('Big chances conceded: {}'.format(round(big_chances_away_conc_pg, 2)))
print('Big chances conceded made(per game): {}'.format(round(big_chances_away_conc_made_pg, 2)))
try:
    print('Expected goals: {}'.format(round(sum(xgAway) / len(xgAway), 2)))
    print('Expected goals conceded: {}'.format(round(sum(xgAwayConc) / len(xgAwayConc), 2)))
except (ZeroDivisionError):
    print('!!!Could not get xG stats!!!')
print('Goals scored: {}'.format(goalsScoredAway))
print('Goals conceded: {}'.format(goalsConcAway))
print(len(big_chances_away))
print(len(big_chances_missed_away))
print('-----------------------------------')
print('home: {}, {}'.format(round((big_chances_home_pg + big_chances_away_conc_pg)/2, 2), round((big_chances_made_pg + big_chances_away_conc_made_pg)/2, 2)))
print('away: {}, {}'.format(round((big_chances_away_pg + big_chances_conc_pg)/2, 2), round((big_chances_away_made_pg + big_chances_conc_made_pg)/2, 2)))
print('{}, {}'.format(round(((big_chances_home_pg + big_chances_away_conc_pg)/2) - ((big_chances_away_pg + big_chances_conc_pg)/2), 2), round(((big_chances_made_pg + big_chances_away_conc_made_pg)/2) - ((big_chances_away_made_pg + big_chances_conc_made_pg)/2), 2)))
print('----------------------------------')
print('Average scores for the match')
print('----------------------------------')
print('{} - {}'.format(round((goalsScoredHome + goalsConcAway) / 2, 2), round((goalsScoredAway + goalsConcHome) / 2, 2)))
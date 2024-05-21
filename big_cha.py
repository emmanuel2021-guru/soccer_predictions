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



seasonId = 58388

teamIdHome = 215186
teamIdAway = 281331
# teamLocation = 1

excludeId = 12060319

teamData = requests.get('https://www.sofascore.com/api/v1/team/{}'.format(teamIdHome), headers=headers)
team = teamData.json()
print(team['team']['name'])
print('---------------------------------')
big_chances_home = []
big_chances_home_conc = []
big_chances_scored_home = []
big_chances_scored_home_conc = []
big_chances_away = []
big_chances_away_conc = []
big_chances_scored_away = []
big_chances_scored_away_conc = []
goalsHome = []
goalsHomeConc = []
goalsAway = []
goalsAwayConc = []
xgHome = []
xgHomeConc = []
xgAway = []
xgAwayConc = []
pointsHome = []
pointsAway = []
crossesHome = []
crossesConcHome = []
crossesAway = []
crossesConcAway = []
cornersHome = []
cornersConcHome = []
cornersAway = []
cornersConcAway = []
for i in range(3):
    response = requests.get('https://www.sofascore.com/api/v1/team/{}/events/last/{}'.format(teamIdHome, i), headers=headers)
    data = response.json()
    for event in data['events']:
        try:
            if event['homeTeam']['id'] == teamIdHome and event['season']['id'] == seasonId and event['id'] != excludeId:
                # ids.append(event['id'])
                # print(event['id'])
                if event['homeScore']['normaltime'] > event['awayScore']['normaltime']:
                    pointsHome.append(3)
                elif event['homeScore']['normaltime'] == event['awayScore']['normaltime']:
                    pointsHome.append(1)
                else:
                    pointsHome.append(0)
                goalsHome.append(event['homeScore']['normaltime'])
                goalsHomeConc.append(event['awayScore']['normaltime'])
                res1 = requests.get('https://api.sofascore.com/api/v1/event/{}/statistics'.format(event['id']), headers=headers)
                data2 = res1.json()
                # print(data2['statistics'][0]['groups'][4]['statisticsItems'][3]['name'])
                # print(data2['statistics'][0]['groups'][3]['statisticsItems'][0]['name'])
                if data2['statistics'][0]['groups'][0]['statisticsItems'][4]['name'] == 'Corner kicks':
                    cornersHome.append(int(data2['statistics'][0]['groups'][0]['statisticsItems'][4]['home']))
                    cornersConcHome.append(int(data2['statistics'][0]['groups'][0]['statisticsItems'][4]['away']))
                elif data2['statistics'][0]['groups'][0]['statisticsItems'][5]['name'] == 'Corner kicks':
                    cornersHome.append(int(data2['statistics'][0]['groups'][0]['statisticsItems'][5]['home']))
                    cornersConcHome.append(int(data2['statistics'][0]['groups'][0]['statisticsItems'][5]['away']))
                res = requests.get('https://api.sofascore.com/api/v1/event/{}/statistics'.format(event['id']), headers=headers)
                data1 = res.json()
                # print("before loop")
                for stat in data1['statistics'][0]['groups']:
                    # if stat[2]['statisticsItems'][0]['name'] == 'Corner kicks':
                    #     temp_corners = int(stat['statistics'][0]['home'])
                    #     cornersHome.append(temp_corners)
                        # print(temp_corners)
                    # print(stat['groupName'])
                    if stat['groupName'] == 'Match overview':
                        if stat['statisticsItems'][1]['name'] == 'Expected goals':
                            # print(type(stat['statisticsItems'][0]['home']))
                            temp_xg = float(stat['statisticsItems'][1]['home'])
                            temp_xg_conc = float(stat['statisticsItems'][1]['away'])
                            xgHome.append(temp_xg)
                            xgHomeConc.append(temp_xg_conc)
                        if stat['statisticsItems'][2]['name'] == 'Big chances':
                            temp_big_cha = int(stat['statisticsItems'][2]['home'])
                            temp_big_cha_conc = int(stat['statisticsItems'][2]['away'])
                            big_chances_home.append(temp_big_cha)
                            big_chances_home_conc.append(temp_big_cha_conc)
                            # print('big chances')
                            # print('---------------------------------')
                            # print(temp_big_cha, temp_big_cha_conc)
                        if stat['statisticsItems'][1]['name'] == 'Big chances':
                            temp_big_cha = int(stat['statisticsItems'][1]['home'])
                            temp_big_cha_conc = int(stat['statisticsItems'][1]['away'])
                            big_chances_home.append(temp_big_cha)
                            big_chances_home_conc.append(temp_big_cha_conc)
                            # print('big chances')
                            # print('---------------------------------')
                            # print(temp_big_cha, temp_big_cha_conc)
                    elif stat['groupName'] == 'Attack':
                        if stat['statisticsItems'][0]['name'] == 'Big chances scored':
                            # print('big chances missed')
                            # print('--------------------------------')
                            temp_big_cha_sco = int(stat['statisticsItems'][0]['home'])
                            temp_big_cha_sco_conc = int(stat['statisticsItems'][0]['away'])
                            big_chances_scored_home.append(temp_big_cha_sco)
                            big_chances_scored_home_conc.append(temp_big_cha_sco_conc)
                            # print(temp_big_cha_miss, temp_big_cha_miss_conc)
                        else:
                            temp_big_cha_sco = 0
                            temp_big_cha_sco_conc = 0
                            big_chances_scored_home.append(temp_big_cha_sco)
                            big_chances_scored_home_conc.append(temp_big_cha_sco_conc)
                    elif stat['groupName'] == 'Passes':
                        # print(stat['statisticsItems'][3]['name'])
                        if stat['statisticsItems'][4]['name'] == 'Crosses':
                            # print(type(stat['statisticsItems'][0]['home']))
                            temp_cross = stat['statisticsItems'][4]['homeTotal']
                            temp_cross_conc = stat['statisticsItems'][4]['awayTotal']
                            crossesHome.append(temp_cross)
                            crossesConcHome.append(temp_cross_conc)
                # res1 = requests.get('https://api.sofascore.com/api/v1/event/{}/statistics'.format(event['id']), headers=headers)
                # data2 = res1.json()
                # # print(data2['statistics'][0]['groups'][3]['statisticsItems'][0]['name'])
                # if data2['statistics'][0]['groups'][3]['statisticsItems'][0]['name'] == 'Corner kicks':
                #     temp_corners = int(stat['statistics'][0]['home'])
                
                
                
                # for stat1 in data1['statistics'][0]['groups']:
                #     if stat1['groupName'] == 'TVData':
                #         if stat1['statisticsItems'][0]['name'] == 'Corner kicks':
                #             temp_corners = int(stat['statistics'][0]['home'])
                #             print(temp_corners)
                
                # cornersPerCrossHome.append(round(temp_corners / temp_cross, 2))
        except (TypeError, KeyError, NameError):
            continue
try:
    big_chances_home_pg = sum(big_chances_home)/len(big_chances_home)
    big_chances_made_pg = sum(big_chances_scored_home)/len(big_chances_scored_home)
    big_chances_conc_pg = sum(big_chances_home_conc)/len(big_chances_home_conc)
    big_chances_conc_made_pg = sum(big_chances_scored_home_conc) / len(big_chances_scored_home_conc)
except (ZeroDivisionError):
    print("!!!Could not get big chances stats!!!")
goalsScoredHome = round(sum(goalsHome) / len(goalsHome), 2)
goalsConcHome = round(sum(goalsHomeConc) / len(goalsHomeConc), 2)
try:
    print('{}: {}'.format(stat['statisticsItems'][0]['name'], round(big_chances_home_pg, 2)))
    print('Big chances made(per game): {}'.format(round(big_chances_made_pg, 2)))
    print('Big chances conceded: {}'.format(round(big_chances_conc_pg, 2)))
    print('Big chances conceded made(per game): {}'.format(round(big_chances_conc_made_pg, 2)))
except (NameError):
    print("!!!Could not get big chances stats!!!")
try:
    print('Expected goals: {}'.format(round(sum(xgHome) / len(xgHome), 2)))
    print('Expected goals conceded: {}'.format(round(sum(xgHomeConc) / len(xgHomeConc), 2)))
except (ZeroDivisionError):
    print('!!!Could not get xG stats!!!')
print('Goals scored: {}'.format(goalsScoredHome))
print('Goals conceded: {}'.format(goalsConcHome))
# print('corners: {}'.format(cornersHome))
print(len(big_chances_home))
print(len(big_chances_scored_home))
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
                if event['awayScore']['normaltime'] > event['homeScore']['normaltime']:
                    pointsAway.append(3)
                elif event['awayScore']['normaltime'] == event['homeScore']['normaltime']:
                    pointsAway.append(1)
                else:
                    pointsAway.append(0)
                goalsAway.append(event['awayScore']['normaltime'])
                goalsAwayConc.append(event['homeScore']['normaltime'])
                # res1 = requests.get('https://api.sofascore.com/api/v1/event/{}/statistics'.format(event['id']), headers=headers)
                # data2 = res1.json()
                # print(data2['statistics'][0]['groups'][3]['statisticsItems'][0]['name'])
                # cornersAway.append(int(['statistics'][0]['groups'][3]['statisticsItems'][0]['away']))
                res1 = requests.get('https://api.sofascore.com/api/v1/event/{}/statistics'.format(event['id']), headers=headers)
                data2 = res1.json()
                # # print(data2['statistics'][0]['groups'][3]['statisticsItems'][0]['name'])
                # cornersAway.append(int(data2['statistics'][0]['groups'][3]['statisticsItems'][0]['away']))
                if data2['statistics'][0]['groups'][0]['statisticsItems'][4]['name'] == 'Corner kicks':
                    cornersAway.append(int(data2['statistics'][0]['groups'][0]['statisticsItems'][4]['away']))
                    cornersConcAway.append(int(data2['statistics'][0]['groups'][0]['statisticsItems'][4]['home']))
                elif data2['statistics'][0]['groups'][0]['statisticsItems'][5]['name'] == 'Corner kicks':
                    cornersAway.append(int(data2['statistics'][0]['groups'][0]['statisticsItems'][5]['away']))
                    cornersConcAway.append(int(data2['statistics'][0]['groups'][0]['statisticsItems'][5]['home']))
                res = requests.get('https://api.sofascore.com/api/v1/event/{}/statistics'.format(event['id']), headers=headers)
                data1 = res.json()
                for stat in data1['statistics'][0]['groups']:
                    if stat['groupName'] == 'Match overview':
                        if stat['statisticsItems'][1]['name'] == 'Expected goals':
                            temp_xg = float(stat['statisticsItems'][1]['away'])
                            temp_xg_conc = float(stat['statisticsItems'][1]['home'])
                            xgAway.append(temp_xg)
                            xgAwayConc.append(temp_xg_conc)
                    # if stat['groupName'] == 'TVData':
                    #     if stat['statisticsItems'][0]['name'] == 'Corner kicks':
                    #         temp_corners = int(stat['statistics'][0]['away'])
                        if stat['statisticsItems'][2]['name'] == 'Big chances':
                            temp_big_cha = int(stat['statisticsItems'][2]['away'])
                            temp_big_cha_conc = int(stat['statisticsItems'][2]['home'])
                            big_chances_away.append(temp_big_cha)
                            big_chances_away_conc.append(temp_big_cha_conc)
                            # print('big chances')
                            # print('---------------------------------')
                            # print(temp_big_cha, temp_big_cha_conc)
                        if stat['statisticsItems'][1]['name'] == 'Big chances':
                            temp_big_cha = int(stat['statisticsItems'][1]['away'])
                            temp_big_cha_conc = int(stat['statisticsItems'][1]['home'])
                            big_chances_away.append(temp_big_cha)
                            big_chances_away_conc.append(temp_big_cha_conc)
                            # print('big chances')
                            # print('---------------------------------')
                            # print(temp_big_cha, temp_big_cha_conc)
                    elif stat['groupName'] == 'Attack':
                        if stat['statisticsItems'][0]['name'] == 'Big chances scored':
                            temp_big_cha_sco = int(stat['statisticsItems'][0]['away'])
                            temp_big_cha_sco_conc = int(stat['statisticsItems'][0]['home'])
                            big_chances_scored_away.append(temp_big_cha_sco)
                            big_chances_scored_away_conc.append(temp_big_cha_sco_conc)
                            # print('big chances missed')
                            # print('--------------------------------')
                            # print(temp_big_cha_miss, temp_big_cha_miss_conc)
                        else:
                            temp_big_cha_sco = 0
                            temp_big_cha_sco_conc = 0
                            big_chances_scored_away.append(temp_big_cha_sco)
                            big_chances_scored_away_conc.append(temp_big_cha_sco_conc)
                    elif stat['groupName'] == 'Passes':
                        if stat['statisticsItems'][4]['name'] == 'Crosses':
                            # print(type(stat['statisticsItems'][0]['home']))
                            # print('here')
                            # temp_cross = stat['statisticsItems'][4]['awayTotal']
                            # temp_cross_conc = stat['statisticsItems'][4]['homeTotal']
                            crossesAway.append(stat['statisticsItems'][4]['awayTotal'])
                            crossesConcAway.append(stat['statisticsItems'][4]['homeTotal'])
                    #         # print('-----------------------------')
                    #         # print('temp_cross')
                    #         # print('------------------------------')
                    #         # print(temp_cross)
                # res1 = requests.get('https://api.sofascore.com/api/v1/event/{}/statistics'.format(event['id']), headers=headers)
                # data2 = res1.json()
                # # print(data2['statistics'][0]['groups'][3]['statisticsItems'][0]['name'])
                # if data2['statistics'][0]['groups'][3]['statisticsItems'][0]['name'] == 'Corner kicks':
                #     temp_corners = int(stat['statistics'][0]['away'])
                
                
                
                # for stat2 in data1['statistics'][0]['groups']:
                #     if stat2['groupName'] == 'TVData':
                #         if stat2['statisticsItems'][0]['name'] == 'Corner kicks':
                #             temp_corners = int(stat['statistics'][0]['home'])
                  
        except (TypeError, KeyError, NameError):
            continue
try:
    big_chances_away_pg = sum(big_chances_away)/len(big_chances_away)
    big_chances_away_made_pg = sum(big_chances_scored_away)/len(big_chances_scored_away)
    big_chances_away_conc_pg = sum(big_chances_away_conc)/len(big_chances_away_conc)
    big_chances_away_conc_made_pg = sum(big_chances_scored_away_conc)/len(big_chances_scored_away_conc)
except (ZeroDivisionError):
    print('!!!Could not get big chances stats!!!')
goalsScoredAway = round(sum(goalsAway) / len(goalsAway), 2)
goalsConcAway = round(sum(goalsAwayConc) / len(goalsAwayConc), 2)
try:
    print('{}: {}'.format(stat['statisticsItems'][0]['name'], round(big_chances_away_pg, 2)))
    print('Big chances made(per game): {}'.format(round(big_chances_away_made_pg, 2)))
    print('Big chances conceded: {}'.format(round(big_chances_away_conc_pg, 2)))
    print('Big chances conceded made(per game): {}'.format(round(big_chances_away_conc_made_pg, 2)))
except (NameError):
    print("!!!Could not get big chances stats!!!")
try:
    print('Expected goals: {}'.format(round(sum(xgAway) / len(xgAway), 2)))
    print('Expected goals conceded: {}'.format(round(sum(xgAwayConc) / len(xgAwayConc), 2)))
except (ZeroDivisionError):
    print('!!!Could not get xG stats!!!')
print('Goals scored: {}'.format(goalsScoredAway))
print('Goals conceded: {}'.format(goalsConcAway))
print(len(big_chances_away))
print(len(big_chances_scored_away))
print('-----------------------------------')
try:
    # print(big_chances_home)
    print('home: {}, {}'.format(round((big_chances_home_pg + big_chances_away_conc_pg)/2, 2), round((big_chances_made_pg + big_chances_away_conc_made_pg)/2, 2)))
    print('away: {}, {}'.format(round((big_chances_away_pg + big_chances_conc_pg)/2, 2), round((big_chances_away_made_pg + big_chances_conc_made_pg)/2, 2)))
    print('{}, {}'.format(round(((big_chances_home_pg + big_chances_away_conc_pg)/2) - ((big_chances_away_pg + big_chances_conc_pg)/2), 2), round(((big_chances_made_pg + big_chances_away_conc_made_pg)/2) - ((big_chances_away_made_pg + big_chances_conc_made_pg)/2), 2)))
except (NameError):
    print("!!!Could not get big chances stats!!!")
print('----------------------------------')
print('Points per game')
print('----------------------------------')
print('Home: {}'.format(round(sum(pointsHome) / len(pointsHome), 2)))
print('Away: {}'.format(round(sum(pointsAway) / len(pointsAway), 2)))
print('----------------------------------')
print('Average scores for the match')
print('----------------------------------')
print('{} - {}'.format(round((goalsScoredHome + goalsConcAway) / 2, 2), round((goalsScoredAway + goalsConcHome) / 2, 2)))
print('----------------------------------')
print('Crosses per game')
print(len(cornersHome), len(crossesHome), len(crossesConcHome))
print(len(cornersAway), len(crossesAway), len(crossesConcAway))
print('----------------------------------')
try:
    print('Home: {}'.format(round(((sum(crossesHome) / len(crossesHome)) + (sum(crossesConcAway) / len(crossesConcAway)))/2, 2)))
    print('Away: {}'.format(round(((sum(crossesAway) / len(crossesAway)) + (sum(crossesConcHome) / len(crossesConcHome)))/2, 2)))
except (ZeroDivisionError):
    print('!!!Crosses data not found!!!')
print('----------------------------------')
print('Corners per game')
print('----------------------------------')
try:
    print('Home: {}'.format(round(((sum(cornersHome) / len(cornersHome)) + (sum(cornersConcAway) / len(cornersConcAway))/2), 2)))
    print('Away: {}'.format(round(((sum(cornersAway) / len(cornersAway)) + (sum(cornersConcHome) / len(cornersConcHome))/2), 2)))
except (ZeroDivisionError):
    print('!!!Corner data not found!!!')
print('----------------------------------')
try:
    print('Home: {}'.format(round(sum(cornersHome) / len(cornersHome), 2)))
    print(cornersHome)
    print('Away: {}'.format(round(sum(cornersAway) / len(cornersAway), 2)))
except (ZeroDivisionError):
    print('!!!Corner data not found!!!')
print('----------------------------------')
try:
    print('Home: {}'.format(round(sum(cornersConcAway) / len(cornersConcAway), 2)))
    print(cornersConcHome)
    print('Away: {}'.format(round(sum(cornersConcHome) / len(cornersConcHome), 2)))
except (ZeroDivisionError):
    print('!!!Corner data not found!!!')
print('----------------------------------')
print('Corners per cross')
print('----------------------------------')
# print('Home: {}, Away: {}'.format(round(sum(cornersHome) / sum(crossesHome), 2), round(sum(cornersPerCrossAway)/len(cornersPerCrossAway), 2)))
print('{}, {}'.format(len(cornersHome), len(crossesHome)))
print('{}, {}'.format(len(cornersAway), len(crossesAway)))
print('-----------------------------------')
print('Home: {}, Away: {}'.format(round(sum(cornersHome) / sum(crossesHome), 2), round(sum(cornersAway) / sum(crossesAway), 2)))
print('-----------------------------------')
print('Predicted corners')
print('-----------------------------------')
homeCross = ((sum(crossesHome) / len(crossesHome)) + (sum(crossesConcAway) / len(crossesConcAway)))/2
awayCross = ((sum(crossesAway) / len(crossesAway)) + (sum(crossesConcHome) / len(crossesConcHome)))/2
homeCPC = ((sum(cornersHome) + sum(cornersConcAway))/2) / sum(crossesHome)
awayCPC = ((sum(cornersAway) + sum(cornersConcHome))/2) / sum(crossesAway)
print('Home: {}, Away: {}, Total: {}'.format(round(homeCross * homeCPC, 2), round(awayCross * awayCPC, 2), round((homeCross * homeCPC) + (awayCross * awayCPC), 2)))
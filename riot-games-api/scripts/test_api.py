import requests
import pandas as pd
from time import sleep

API_KEY = "RGAPI-2e2b17f0-0894-4644-9d61-2e80c1e78118"
player_puuid = 'F5podb4uVbhW8unGNzmVSCYB3wxjlYoKJEcver1FqpjzcG1tuWCvxlXEvsnaf-hEK9llgHJolCyObQ'

""" r_url_summoner = f"https://la2.api.riotgames.com/lol/league/v4/entries/by-summoner/QhJ7ZgCgCBv26eLVOU_FGeBTozxmvZXh_dKEICC-ygRQIcM?api_key={API_KEY}"

r = requests.get(r_url_summoner)

if r.status_code == 200:
    player_league_info = r.json()
else:
    print(r.status_code, r.content)

filtred_stats = {
    'wins': player_league_info[1]['wins'],
    'losses': player_league_info[1]['losses']
}


print(filtred_stats) """

r_url_matches = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/F5podb4uVbhW8unGNzmVSCYB3wxjlYoKJEcver1FqpjzcG1tuWCvxlXEvsnaf-hEK9llgHJolCyObQ/ids?api_key={API_KEY}&type=ranked&start=0&count=100"

r = requests.get(r_url_matches)

if r.status_code == 200:
    player_matches_id = r.json()
else:
    print(f"URL MATCHES ERROR: {r.status_code}, {r.content}")

#----------------------------------------------------------------------------------------------------

r_url_matches_info = f'https://americas.api.riotgames.com/lol/match/v5/matches/{player_matches_id[0]}?api_key={API_KEY}'

r = requests.get(r_url_matches_info)

if r.status_code == 200:
    player_matches_info = r.json()
else:
    print(f"URL MATCHES IDS ERROR: {r.status_code}, {r.content}")

#----------------------------------------------------------------------------------------------------

part_index = player_matches_info['metadata']['participants'].index(player_puuid)
player_matches_info['info']['participants'][part_index]

match_details_list = []

for match in player_matches_id:

    r_url_matches_info = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match}?api_key={API_KEY}'

    r = requests.get(r_url_matches_info)

    if r.status_code == 200:
        player_matches_info = r.json()
    else:
        print(f"URL MATCHES INFO ERROR: {r.status_code}, {r.content}")

    part_index = player_matches_info['metadata']['participants'].index(player_puuid)

    #Quiero guardar el valor del team para luego sacar las stats correspondientes.
    #team_id = player_matches_info['info']['participants'][part_index]['teamId']

    filtred_stats = {
        'matchId': player_matches_info['metadata']['matchId'],
        'gameId': player_matches_info['info']['gameId'],
        'gameCreation': player_matches_info['info']['gameCreation'],
        'gameStartTimestamp': player_matches_info['info']['gameStartTimestamp'],
        'gameEndTimestamp': player_matches_info['info']['gameEndTimestamp'],
        'gameDuration': player_matches_info['info']['gameDuration'],
        'endOfGameResult': player_matches_info['info']['endOfGameResult'],
        'win': player_matches_info['info']['participants'][part_index]['win'],

        'individualPosition': player_matches_info['info']['participants'][part_index]['individualPosition'],
        'lane': player_matches_info['info']['participants'][part_index]['lane'],
        'championId': player_matches_info['info']['participants'][part_index]['championId'],
        'championName': player_matches_info['info']['participants'][part_index]['championName'],
        'champLevel': player_matches_info['info']['participants'][part_index]['champLevel'],

        'kills': player_matches_info['info']['participants'][part_index]['kills'],
        'deaths': player_matches_info['info']['participants'][part_index]['deaths'],
        'assists': player_matches_info['info']['participants'][part_index]['assists'],
        'kda': player_matches_info['info']['participants'][part_index]['challenges']['kda'],
        'killParticipation': player_matches_info['info']['participants'][part_index]['challenges']['killParticipation'],

        'spell1Casts': player_matches_info['info']['participants'][part_index]['spell1Casts'],
        'spell2Casts': player_matches_info['info']['participants'][part_index]['spell2Casts'],
        'spell3Casts': player_matches_info['info']['participants'][part_index]['spell3Casts'],
        'spell4Casts': player_matches_info['info']['participants'][part_index]['spell4Casts'],
        'abilityUses': player_matches_info['info']['participants'][part_index]['challenges']['abilityUses'],

        'neutralMinionsKilled': player_matches_info['info']['participants'][part_index]['neutralMinionsKilled'],
        'totalAllyJungleMinionsKilled': player_matches_info['info']['participants'][part_index]['totalAllyJungleMinionsKilled'],
        'totalEnemyJungleMinionsKilled': player_matches_info['info']['participants'][part_index]['totalEnemyJungleMinionsKilled'],
        'totalMinionsKilled': player_matches_info['info']['participants'][part_index]['totalMinionsKilled'],

        'kills': player_matches_info['info']['participants'][part_index]['kills'],
        'kills': player_matches_info['info']['participants'][part_index]['kills'],
        'kills': player_matches_info['info']['participants'][part_index]['kills'],

    }

    match_details_list.append(filtred_stats)
    sleep(1)


df_match_stats = pd.DataFrame(match_details_list)

print(df_match_stats)


"""     'individualPosition': player_matches_info['info']['participants'][part_index]['individualPosition'],
        'lane': player_matches_info['info']['participants'][part_index]['lane'],
        'championId': player_matches_info['info']['participants'][part_index]['championId'],
        'championName': player_matches_info['info']['participants'][part_index]['championName'],
        'champLevel': player_matches_info['info']['participants'][part_index]['champLevel'],

        'kills': player_matches_info['info']['participants'][part_index]['kills'],
        'deaths': player_matches_info['info']['participants'][part_index]['deaths'],
        'assists': player_matches_info['info']['participants'][part_index]['assists'],
        'kda': player_matches_info['info']['participants'][part_index]['challenges']['kda'],
        'killParticipation': player_matches_info['info']['participants'][part_index]['challenges']['killParticipation'],

        'spell1Casts': player_matches_info['info']['participants'][part_index]['spell1Casts'],
        'spell2Casts': player_matches_info['info']['participants'][part_index]['spell2Casts'],
        'spell3Casts': player_matches_info['info']['participants'][part_index]['spell3Casts'],
        'spell4Casts': player_matches_info['info']['participants'][part_index]['spell4Casts'],
        'abilityUses': player_matches_info['info']['participants'][part_index]['challenges']['abilityUses'],

        'neutralMinionsKilled': player_matches_info['info']['participants'][part_index]['neutralMinionsKilled'],
        'totalAllyJungleMinionsKilled': player_matches_info['info']['participants'][part_index]['totalAllyJungleMinionsKilled'],
        'totalEnemyJungleMinionsKilled': player_matches_info['info']['participants'][part_index]['totalEnemyJungleMinionsKilled'],
        'totalMinionsKilled': player_matches_info['info']['participants'][part_index]['totalMinionsKilled'],

        'kills': player_matches_info['info']['participants'][part_index]['kills'],
        'kills': player_matches_info['info']['participants'][part_index]['kills'],
        'kills': player_matches_info['info']['participants'][part_index]['kills'], """
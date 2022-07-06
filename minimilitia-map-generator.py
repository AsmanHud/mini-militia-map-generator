import random, time

def format_time(seconds):
    return [seconds//3600, seconds%3600//60, seconds%3600%60]

def last_n_elems(lst, n):
    if n == 0:
        return []
    if len(lst) <= n:
        return lst
    return lst[-n:]

available_maps = [
"Outpost", "Sniper Outpost", "Jungle", "Undermine", "Overseer", "Suspension", "Cliffhanger",
"Alienate", "No Escape", "Subdivision", "Vantage", "Icebox", "High Tower", "Bottleneck",
"Snow Blind", "Catacombs", "Pyramid", "So Long", "Underground", "Lunarcy", "Junkyard",
"Crossfire", "Mini Outpost"
]

print("Welcome to Minimilitia bot!")
print("First enter maps you will play.\nEnter 'all' to play all of standart maps, enter 'q' to finish.\n"
"You can write any map names (in case you have custom maps). Standart maps list (according to latest version):\n\n"
'Outpost, Sniper Outpost, Jungle, Undermine, Overseer, Suspension, Cliffhanger,\n'
'Alienate, No Escape, Subdivision, Vantage, Icebox, High Tower, Bottleneck, Snow Blind,\n'
'Catacombs, Pyramid, So Long, Underground, Lunarcy, Junkyard, Crossfire, Mini Outpost\n')
maps_to_play = []
amap = input("Map name: ")
if amap == "all":
    maps_to_play = available_maps
elif amap == "q":
    pass
else:
    while True:
        if amap in maps_to_play:
            print("Map has not been added: it is already in the list.")
        else:
            maps_to_play.append(amap)
        amap = input("Map name: ")
        if amap == "q":
            break
print()

played_maps_history = []
pseudo_last_two = []
while len(pseudo_last_two) != 2:
    if len(maps_to_play) < 3:
        break
    pseudo_last_two.append(random.choice(maps_to_play))
    pseudo_last_two = list(set(pseudo_last_two))

start = time.time()

if len(maps_to_play) < 3:
    # Case if 0 maps are chosen
    if len(maps_to_play) == 0:
        exit()
    # Case if only one map was chosen
    elif len(maps_to_play) == 1:
        amap = maps_to_play[0]
        while True:
            print("Last maps played: "+("" if len(played_maps_history)==0 else amap))
            print("=============\n"
            "Map to play: "+amap+"\n"
            "=============")
            played_maps_history.append(amap)
            question = input("Play another game? (ENTER = yes, 'q' = no): ")
            if question == "q":
                break
            print()
    # Case if two maps were chosen
    else:
        i = random.randint(0, 1)
        while True:
            amap = maps_to_play[i%2]
            print("Last maps played: "+("..., " if len(played_maps_history) > 3 else "")+", ".join(last_n_elems(played_maps_history, 3)))
            print("=============\n"
            "Map to play: "+amap+"\n"
            "=============")
            played_maps_history.append(amap)
            question = input("Play another game? (ENTER = yes, 'q' = no): ")
            if question == "q":
                break
            i += 1
            print()
# Case if three or more maps were chosen
else:
    # First four games
    i = 0
    while i != 4:
        amap = random.choice(maps_to_play)
        if amap in pseudo_last_two:
            continue
        print("Last maps played: "+", ".join(last_n_elems(played_maps_history, 3)))
        print("=============\n"
            "Map to play: "+amap+"\n"
            "=============")
        played_maps_history.append(amap)
        pseudo_last_two.append(amap)
        pseudo_last_two.pop(0)
        question = input("Play another game? (ENTER = yes, 'q' = no): ")
        if question == "q":
            break
        i += 1
        print()
    del pseudo_last_two # deleting variable felt satisfying, even if it is not nessesary

    # Main cycle
    while True:
        amap = random.choice(maps_to_play)
        if amap in played_maps_history[-2:]:
            continue
        print("Last maps played: ..., "+", ".join(last_n_elems(played_maps_history, 3)))
        print("=============\n"
            "Map to play: "+amap+"\n"
            "=============")
        played_maps_history.append(amap)
        question = input("Play another game? (ENTER = yes, 'q' = no): ")
        if question == "q":
            break
        print()

end = time.time()

# Statistics
time_spent_in_seconds = round(end - start)
time_spent = format_time(time_spent_in_seconds)
games_played = len(played_maps_history)
avg_time = format_time(round(time_spent_in_seconds / games_played))
count_maps = sorted([(amap, played_maps_history.count(amap)) for amap in maps_to_play], key=lambda x: x[1], reverse=True)
if len(count_maps) < 3:
    while len(count_maps) != 3:
        count_maps.append(("-", 0))

print(f"""------------------------------------------------------------------------------------------
Statistics:
Games played: {games_played}
Time spent: {time_spent[0]} hours, {time_spent[1]} minutes, {time_spent[2]} seconds
Average time spent on a game: {avg_time[1]} minutes, {avg_time[2]} seconds
Most played maps: {count_maps[0][0]} ({count_maps[0][1]} times or {round((count_maps[0][1]/games_played)*100, 2)}%)
                  {count_maps[1][0]} ({count_maps[1][1]} times or {round((count_maps[1][1]/games_played)*100, 2)}%)
                  {count_maps[2][0]} ({count_maps[2][1]} times or {round((count_maps[2][1]/games_played)*100, 2)}%)
Full history of maps played:""")
line_len = 0
for amap in played_maps_history[:-1]:
    print(amap + ", ", end="")
    line_len += len(amap)+2
    if line_len > 70:
        print()
        line_len = 0
print(played_maps_history[-1]+".\n")
input("Press ENTER to exit...")
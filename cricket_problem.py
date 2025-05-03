player_name=input("Enter player name :")
player_runs=int(input(f"Enter a number of Runs Scored by {player_name} :"))
player_balls_played=int(input(f"how many  balls  played by {player_name} : "))
strike_rate=player_runs / player_balls_played * 100
print(f"{player_name} Scored {player_runs} runs  in {player_balls_played} by the Strike rate of {strike_rate}")


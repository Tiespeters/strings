# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
# Players that scored in the Final
scored_player1 = 'Ruud Gullit'
scored_player2 = 'Marco van Basten'

#Minutes of the match a goal was scored
goal_0 = 32
goal_1 = 54

scorers = f'{scored_player1} {goal_0}, {scored_player2} {goal_1}'
report = f'{scored_player1} scored in the {goal_0}nd minute\n{scored_player2} scored in the {goal_1}th minute'

# Part 2
player = 'Ronald Koeman'
first_name = player[0:6]
last_name_len = len(player[7:])

name_short = f'{player[0:1]}. {player[7:]}'
chant = f'{first_name}!\t'*6
good_chant = (chant[7:7] !='')










import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    # Define strategies
    def random_strategy():
        return random.choice(['R', 'P', 'S'])
    
    def counter_strategy():
        if not opponent_history:
            return random_strategy()
        counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
        return counter_moves[opponent_history[-1]]
    
    def frequency_strategy():
        if not opponent_history:
            return random_strategy()
        move_count = {'R': 0, 'P': 0, 'S': 0}
        for move in opponent_history:
            move_count[move] += 1
        most_common_move = max(move_count, key=move_count.get)
        counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
        return counter_moves[most_common_move]
    
    def pattern_strategy():
        if len(opponent_history) < 3:
            return random_strategy()
        pattern = ''.join(opponent_history[-3:])
        if pattern == 'RRR':
            return 'P'
        elif pattern == 'PPP':
            return 'S'
        elif pattern == 'SSS':
            return 'R'
        else:
            return random_strategy()
    
    # Select and apply a strategy
    if len(opponent_history) < 100:
        return random_strategy()
    elif len(opponent_history) < 200:
        return counter_strategy()
    elif len(opponent_history) < 300:
        return frequency_strategy()
    else:
        return pattern_strategy()

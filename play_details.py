import random
from tabulate import tabulate
from functools import reduce


class Player:
    """
    Player class represent a player and their capabilities
    """
    no_of_players = 0
    all_players = []
    no_of_rounds = 3
    cube1 = list(range(1, 7))
    cube2 = ['CMB', 'TYK', 'NY', 'LON', 'ATN', 'SYN']
    cube3 = [True, False]

    def __init__(self, name):
        self.name = name
        self.play_count = 0
        self.result = []
        self.final_anlysed_data = {}
        Player.no_of_players += 1
        Player.all_players.append(self)

    def play(self):
        """
        function to assign random lucky draws of cubes
        :return: dictionary consist of random values got from each cube
        """
        if self.play_count < Player.no_of_rounds:
            d = {'first': random.choice(Player.cube1), 'second': random.choice(Player.cube2), 'third': random.choice(Player.cube3)}
            self.result.append(d)
            self.play_count += 1
            return self.result
        else:
            return -1

    def get_total_score(self):
        """
        function to calculate the total score for all 3 rounds
        :return: return total score after 3 rounds
        """
        value_list = list(map(lambda x: x['first'] if x['third']==True else -1*x['first'], self.result))
        total = reduce(lambda x, b: x+b, value_list)
        self.final_anlysed_data['total_score'] = total
        return total

    def get_total_with_para(self, list_dictionaries):
        """

        :param list_dictionaries: list of dictionary values
        :return: total score after 3 rounds
        """
        value_list = list(map(lambda x: x['first'] if x['third']==True else -1*x['first'], list_dictionaries))
        total = reduce(lambda x, b: x+b, value_list)
        return total

    def get_final_score_for_round(self, game_round):
        """

        :param game_round: game round
        :return: total score for the round
        """
        if game_round['third']:
            return game_round['first']
        else:
            return -1 * game_round['first']

    def analyse_by_country(self):
        """
        function to analyse country details got from 3 rounds
        :return: list of categorized data
        """
        categorized_list = []
        l1 = [self.result[0]['second'], self.result[1]['second'], self.result[2]['second']]
        l2 = list(set(l1))

        for i in range(0, len(l2)):
            filter_l = filter(lambda x: x['second'] == l2[i], self.result)
            value = self.get_total_with_para(filter_l)
            country_dictionary = {'second': l2[i], 'value': value}
            self.final_anlysed_data[l2[i]] = value
            categorized_list.append(country_dictionary)
        return categorized_list

    def view_round_results(self):
        """
        function to view round details of a player
        :return: list of final analyzed data
        """
        print('\n--------------Round Details---------------\n')
        tabulate_list = []
        self.get_total_score()
        self.analyse_by_country()
        # self.get_final_winner()
        for dic in self.result:
            tabulate_list.append(['1st round', (dic['first'], dic['second'], dic['third']), 'you have earned '+str(self.get_final_score_for_round(dic))+' at '+dic['second']])
        print(tabulate([tabulate_list[0], tabulate_list[1], tabulate_list[2]], headers=['Round', 'Result', 'meaning of the result']))
        keys = list(self.final_anlysed_data)
        keys.remove('total_score')
        print('\n--------------Final Result after 3 Rounds of player {}---------------\n'.format(self.name))
        print('total score : '+str(self.final_anlysed_data['total_score'])+'\ncity scores :-')
        for i in range(len(keys)):
            print('\r '+keys[i]+' : '+str(self.final_anlysed_data[keys[i]]))
        return self.final_anlysed_data

    @staticmethod
    def get_match_results(self):
        """
        function to evaluate the winner of the game
        :param self:
        :return: name of the winner
        """
        self.get_total_score()
        self.analyse_by_country()
        max_score = Player.all_players[0].get_total_score()
        winner = ''
        for i in Player.all_players:
            if i.get_total_score() >= max_score:
                max_score = i.get_total_score()
                winner = i
        return winner.name

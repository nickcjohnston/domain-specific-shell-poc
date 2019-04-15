import random 

class Goblin():
    name = "Goblin"
    info = "Generates goblins"
    options = {
        'quantity':1,
        'output_format':'csv'
    }

    def __format_output(self, attack, defense, health):
        output = ""
        if self.options['output_format'] == 'csv':
            output = "{0},{1},{2}\n".format(attack, defense, health)
        elif self.options['output_format'] == 'tsv':
            output = "{0}\t{1}\t{2}\n".format(attack, defense, health)
        else:
            output = "{0} {1} {2}\n".format(attack, defense, health)

        return output

    def run(self):
        random.seed()
        output = "Attack,Defense,Health\n"
        if self.options['output_format'] == 'tsv':
            output = output.replace(',', '\t')
        elif self.options['output_format'] not in ['csv', 'tsv']:
            output = output.replace(',', ' ')
        for i in range(0, int(self.options['quantity'])):
            # Attack is 2d6
            attack = random.randint(1, 6) + random.randint(1, 6)
            # Defense is 2d6
            defense = random.randint(1, 6) + random.randint(1, 6)
            # Health is 1d4
            health = random.randint(1, 4)
            output += self.__format_output(attack, defense, health)
        return output.strip()


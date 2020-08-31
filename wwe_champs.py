# This code creates the class Champion and then it inserts the list of champions in WWE into two dictionaries
# The two dictionaries are for the champions on the main roster and the champions on NXT

class Champion:
    def __init__(self, title, title_holder):
        self.title_belt = title
        self.wrestler = title_holder

wrestler1 = Champion('WWE Champion', 'Drew McIntyre')
wrestler2 = Champion('Intercontinental Champion', 'Jeff Hardy')
wrestler3 = Champion('United States Champion', 'Bobby Lashley')
wrestler4 = Champion('RAW Women\'s Champion', 'Asuka')
wrestler5 = Champion('SmackDown Women\'s Champion', 'Bayley')
wrestler6 = Champion('RAW Tag Team Champions', 'The Street Profits')
wrestler7 = Champion('SmackDown Tag Team Champions', 'Cesaro and Shinsuke Nakamura')
wrestler8 = Champion('Women\'s Tag Team Champions', 'Shayna Baszler and Nia Jax')
wrestler247 = Champion('24/7 Champion', 'Akira Tozawa')

wwe_champ = {}

wwe_champ.update({wrestler1.title_belt : wrestler1.wrestler})
wwe_champ.update({wrestler4.title_belt : wrestler4.wrestler})
wwe_champ.update({wrestler5.title_belt : wrestler5.wrestler})
wwe_champ.update({wrestler2.title_belt : wrestler2.wrestler})
wwe_champ.update({wrestler3.title_belt : wrestler3.wrestler})
wwe_champ.update({wrestler6.title_belt : wrestler6.wrestler})
wwe_champ.update({wrestler7.title_belt : wrestler7.wrestler})
wwe_champ.update({wrestler8.title_belt : wrestler8.wrestler})
wwe_champ.update({wrestler247.title_belt : wrestler247.wrestler})

print(wwe_champ)

nxt_champ = {}

wrestler9 = Champion('NXT Champion', 'Vacant')
wrestler10 = Champion('NXT Women\'s Champion', 'Io Shirai')
wrestler11 = Champion('NXT North American Champion', 'Damian Priest')
wrestler12 = Champion('NXT Tag Team Champions', 'Breezango')
wrestler13 = Champion('NXT Cruiserweight Champion', 'Santos Escobar')

nxt_champ.update({wrestler9.title_belt : wrestler9.wrestler})
nxt_champ.update({wrestler10.title_belt : wrestler10.wrestler})
nxt_champ.update({wrestler11.title_belt : wrestler11.wrestler})
nxt_champ.update({wrestler12.title_belt : wrestler12.wrestler})
nxt_champ.update({wrestler13.title_belt : wrestler13.wrestler})

print(nxt_champ)

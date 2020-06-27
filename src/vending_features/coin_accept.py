class CoinAcceptor(object):
    def __init__(self):
        # keep track of value of coins inserted
        self.coin_value = 0
        # number of coins inserted not in coin return
        self.number_of_coins = 0
        super().__init__()

    def accept_coins(self, coin_inserted: str):
        # this functions will determine the value to assign
        # the coin based on the length first (size)
        # the string is then lowered and sorted and compared (weight)
        # if the coin is invalid, it is sent to the coin_return function
        if len(coin_inserted) == 4:
            if self.weigh_coin(coin_inserted) == 'deim':
                self.coin_value += .10
                self.number_of_coins += 1
        elif len(coin_inserted) == 6:
            if self.weigh_coin(coin_inserted) == 'ceikln':
                self.coin_value += .05
                self.number_of_coins += 1
            else:
                self.coin_return(coin_inserted)
        elif len(coin_inserted) == 7:
            if self.weigh_coin(coin_inserted) == 'aeqrrtu':
                self.coin_value += .25
                self.number_of_coins += 1
            else:
                self.coin_return(coin_inserted)
        else:
            self.coin_return(coin_inserted)
    
    def clear_coins(self):
        self.coin_value = 0
        self.number_of_coins = 0

    def weigh_coin(self, coin_to_weigh:str) -> str:
        # returns the "weight" of the coin
        return ''.join(sorted(coin_to_weigh.lower()))

    def coin_return(self, coin_to_return: str):
        # ust prints that a coin has been sent to Coin Return
        return f'{coin_to_return} sent to Coin Return'

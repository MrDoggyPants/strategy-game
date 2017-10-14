class Deck:  # a queue
    def __init__(self, max_size):
        self.size = 0
        self.front = 0
        self.rear = 0
        self.max_size = max_size
        self.items = []
        for i in range(0, self.max_size):
            self.items.append("")

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.size == self.max_size:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.is_full():
            print("Deck is full!")
        elif self.rear + 1 > self.max_size:
            self.rear = 0
            self.items[self.rear] = item
            self.size += 1
        else:
            self.items[self.rear] = item
            self.size += 1
            self.rear += 1

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            self.size -= 1
            if self.front + 1 > self.max_size:
                self.front = 0
            else:
                self.front += 1
            return self.items[self.front]

class Card:
    def __init__(self, name, description, power_cost, *effect_code):
        self.name = name
        self.desc = description
        self.power = power_cost
        self.effects = list(effect_code)  # *args

    def __str__(self):
        return self.name + " | " + str(self.power) + "\n" + self.desc + "\n" + str(self.effects)

def get_card(key):  # finds and retrieves card in card_dict
    if key in card_dict:
        return card_dict[key]
    else:
        return None

card_dict = {
    "sol" : Card("Soldier", "Basic attack unit.", 2, "none"),
    "eng" : Card("Engineer", "When moving, spawns a troop behind him.", 4, "spawn-back")
    # and so on...
}

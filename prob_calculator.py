import random

class Hat:
    def __init__ (self, **kwargs):
        self.contents = self.contents(**kwargs)
        self.ballinfo = {**kwargs}
        
    def contents(self, **kwargs):
        contentlist = []
        for colours in {**kwargs}.keys():
            for i in range({**kwargs}[colours]):
                contentlist.append(colours)
        return contentlist
        
    def draw(self, balls):
        if balls > len(self.contents):
            return self.contents
        drawn_balls = []
        for i in range(balls):
            draw = random.choice(self.contents)
            self.contents.remove(draw)
            drawn_balls.append(draw)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    results = []
    
    if num_balls_drawn > len(hat.contents):
        num_balls_drawn = len(hat.contents)

    for i in range(num_experiments):
        result = random.sample(hat.contents, k = num_balls_drawn)
        resultdic = {}
        for i in range(len(result)):
            if result[i] not in resultdic.keys():
                resultdic.update({result[i]: 1})
            else:
                resultdic[result[i]] += 1
        results.append(resultdic)
    
    failures = 0
    
    for result in results:
        for colour in expected_balls.keys():
            if colour not in result.keys():
                failures += 1
                break
            elif result[colour] < expected_balls[colour]:
                failures += 1
                break
            else:
                continue

    return 1-(failures/num_experiments) 

        
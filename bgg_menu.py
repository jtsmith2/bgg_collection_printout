import boardgamegeek
import time
from collections import defaultdict
import jinja2
import os

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)

bgg = boardgamegeek.BGGClient()

c = bgg.collection('jtsmith2', exclude_subtype='boardgameexpansion', own=True)

game_ids = []

for game in c:
    game_ids.append(game.id)


games = bgg.game_list(game_ids)

cats = set()
for g in games:
    for c in g.categories:
        cats.add('Category: ' + c)

players = ['Players: 1',
           'Players: 2',
           'Players: 3',
           'Players: 4',
           'Players: 5',
           'Players: 6',
           'Players: 7',
           'Players: 8']

for p in players:
    cats.add(p)
        
context = {
    'games': games,
    'cats': sorted(cats)
}
tex = render('bgg_template.tex', context)

file = open('generated_menu.tex','w')
file.write(tex)
file.close()



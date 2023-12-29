lda_topics = [
  ['game', 'play', 'games', 'new', 'app'],
  ['kids', 'children', 'app', 'animals', 'fun'],
  ['subscription', 'period', 'account', 'charged', 'renewal'],
  ['wordfeud', 'wordsfinder', 'lookup', 'insensitive', 'anagrams'],
  ['campaign', 'mission', 'hadrian', 'dinosaurs', 'turret'],
  ['fish', 'marketplace', 'bigfishgames', 'newsletter', 'virtually'],
  ['tabtale', 'tabtale’s', 'providers', 'sites', 'nail']
]


nmf_topics = [
["game", "center", "simple", "best", "playing"],
["play", "player", "players", "online", "multiplayer"],
["battle", "enemies", "enemy", "war", "weapons"],
["fun", "great", "graphics", "music", "addictive"],
["app", "free", "real", "money", "purchases"],
["new", "games", "unlock", "create", "best"],
["levels", "level", "difficulty","challenging" ,"complete"],
]

ctm_topics = [
  ['puzzle', 'puzzles', 'jigsaw', 'fit', 'animals', 'kids', 'numbers', 'animal', 'paint', 'scratch'],
  ['word', 'number', 'grid', 'sudoku', 'numbers', 'words', 'possible', 'letters', 'column', 'tiles'],
  ['gameplay', 'iphone', 'levels', 'touch', 'arcade', 'com', 'platformer', 'soundtrack', 'best', 'appadvice'],
  ['app', 'puzzles', 'kids', 'puzzle', 'contain', 'fun', 'inside', 'positive', 'com', 'hint'],
  ['levels', 'bubble', 'bubbles', 'popping', 'pop', 'score', 'time', 'shooter', 'level', 'fun'],
  ['new', 'ipad', 'world', 'iphone', 'god', 'best', 'universe', 'ios', 'elements', 'create'],
  ['truck', 'boat', 'iphone', 'wood', 'fun', 'generation', 'snow', 'ipads', 'touches', 'interaction']
]



print("""
\\begin{table}
    \scriptsize
    \centering
    \\begin{tabular}{|c|c|c|c|c|c|c|c|}
    \hline
    & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
    \hline
""")

print("\\textbf{LDA} &")
for topic in lda_topics:
  print("\\makecell{" + "\\\\".join(topic) + "}", "&")
print("\\\\")
print("\hline")

print("\\textbf{NMF} &")
for topic in nmf_topics:
  print("\\makecell{" + "\\\\".join(topic) + "}", "&")
print("\\\\")
print("\hline")

print("\\textbf{CTM} &")
for topic in ctm_topics:
  print("\\makecell{" + "\\\\".join(topic) + "}", "&")
print("\\\\")
print("\hline")


print("""
    \end{tabular}
\caption{The seven most frequently appearing topics in the documents for each model. CTM holds the top 10 words for each topic, the other models 5 top words per topic. The topics are ordered from left to right by their frequency in the documents.}
\label{table:most-frequent-topics}
\end{table}
""")


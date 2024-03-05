#!/bin/usr/python

# This is the list from Appendix C of Comparing Methods for Single Paragraph Similarity Analysis
# 18 August 2010 https://doi-org.libproxy.helsinki.fi/10.1111/j.1756-8765.2010.01108.x
# Benjamin Stone, Simon Dennis, Peter J. Kwantes
#
reference_string ="""
afterwards again against all almost alone along already
also although always am among amongst amoungst amount an and another any anyhow
anyone anything anyway anywhere are around as at back be became because become
becomes becoming been before beforehand behind being below beside besides between
beyond bill both bottom but by call can cannot cant co computer con could couldnt cry de
describe detail do done down due during each eg eight either eleven else elsewhere empty
enough etc even ever every everyone everything everywhere except few fifteen fify fill find
fire first five for former formerly forty found four from front full further get give go had
has hasnt have he hence her here hereafter hereby herein hereupon hers herself him
himself his how however hundred i ie if in inc indeed interest into is it its itself keep last
latter latterly least less ltd made many may me meanwhile might mill mine more
moreover most mostly move much must my myself name namely neither never
nevertheless next nine no nobody none noone nor not nothing now nowhere of off often on
once one only onto or other others otherwise our ours ourselves out over own part per
perhaps please put rather re same see seem seemed seeming seems serious several she
should show side since sincere six sixty so some somehow someone something sometime
sometimes somewhere still such system take ten than that the their them themselves then
thence there thereafter thereby therefore therein thereupon these they thick thin third this
those though three through throughout thru thus to together too top toward towards twelve
twenty two un under until up upon us very via was we well were what whatever when
whence whenever where whereafter whereas whereby wherein whereupon wherever
whether which while whither who whoever whole whom whose why will with within
without would yet you your yours yourself yourselves
"""

# This is the stop word list used in Gensim, https://github.com/piskvorky/gensim/blob/master/gensim/parsing/preprocessing.py
gensim_list = ['all', 'six', 'just', 'less', 'being', 'indeed', 'over', 'move', 'anyway', 'four', 'not', 'own', 'through',
    'using', 'fifty', 'where', 'mill', 'only', 'find', 'before', 'one', 'whose', 'system', 'how', 'somewhere',
    'much', 'thick', 'show', 'had', 'enough', 'should', 'to', 'must', 'whom', 'seeming', 'yourselves', 'under',
    'ours', 'two', 'has', 'might', 'thereafter', 'latterly', 'do', 'them', 'his', 'around', 'than', 'get', 'very',
    'de', 'none', 'cannot', 'every', 'un', 'they', 'front', 'during', 'thus', 'now', 'him', 'nor', 'name', 'regarding',
    'several', 'hereafter', 'did', 'always', 'who', 'didn', 'whither', 'this', 'someone', 'either', 'each', 'become',
    'thereupon', 'sometime', 'side', 'towards', 'therein', 'twelve', 'because', 'often', 'ten', 'our', 'doing', 'km',
    'eg', 'some', 'back', 'used', 'up', 'go', 'namely', 'computer', 'are', 'further', 'beyond', 'ourselves', 'yet',
    'out', 'even', 'will', 'what', 'still', 'for', 'bottom', 'mine', 'since', 'please', 'forty', 'per', 'its',
    'everything', 'behind', 'does', 'various', 'above', 'between', 'it', 'neither', 'seemed', 'ever', 'across', 'she',
    'somehow', 'be', 'we', 'full', 'never', 'sixty', 'however', 'here', 'otherwise', 'were', 'whereupon', 'nowhere',
    'although', 'found', 'alone', 're', 'along', 'quite', 'fifteen', 'by', 'both', 'about', 'last', 'would',
    'anything', 'via', 'many', 'could', 'thence', 'put', 'against', 'keep', 'etc', 'amount', 'became', 'ltd', 'hence',
    'onto', 'or', 'con', 'among', 'already', 'co', 'afterwards', 'formerly', 'within', 'seems', 'into', 'others',
    'while', 'whatever', 'except', 'down', 'hers', 'everyone', 'done', 'least', 'another', 'whoever', 'moreover',
    'couldnt', 'throughout', 'anyhow', 'yourself', 'three', 'from', 'her', 'few', 'together', 'top', 'there', 'due',
    'been', 'next', 'anyone', 'eleven', 'cry', 'call', 'therefore', 'interest', 'then', 'thru', 'themselves',
    'hundred', 'really', 'sincere', 'empty', 'more', 'himself', 'elsewhere', 'mostly', 'on', 'fire', 'am', 'becoming',
    'hereby', 'amongst', 'else', 'part', 'everywhere', 'too', 'kg', 'herself', 'former', 'those', 'he', 'me', 'myself',
    'made', 'twenty', 'these', 'was', 'bill', 'cant', 'us', 'until', 'besides', 'nevertheless', 'below', 'anywhere',
    'nine', 'can', 'whether', 'of', 'your', 'toward', 'my', 'say', 'something', 'and', 'whereafter', 'whenever',
    'give', 'almost', 'wherever', 'is', 'describe', 'beforehand', 'herein', 'doesn', 'an', 'as', 'itself', 'at',
    'have', 'in', 'seem', 'whence', 'ie', 'any', 'fill', 'again', 'hasnt', 'inc', 'thereby', 'thin', 'no', 'perhaps',
    'latter', 'meanwhile', 'when', 'detail', 'same', 'wherein', 'beside', 'also', 'that', 'other', 'take', 'which',
    'becomes', 'you', 'if', 'nobody', 'unless', 'whereas', 'see', 'though', 'may', 'after', 'upon', 'most', 'hereupon',
    'eight', 'but', 'serious', 'nothing', 'such', 'why', 'off', 'a', 'don', 'whereby', 'third', 'i', 'whole', 'noone',
    'sometimes', 'well', 'amoungst', 'yours', 'their', 'rather', 'without', 'so', 'five', 'the', 'first', 'with',
    'make', 'once']

reference_array = reference_string.split()
print(sorted(reference_array))
print(sorted(gensim_list))

print("Length of Stone, Dennis, Kwantes stopword list", len(reference_array))
print("Length of Gensim stopword list", len((gensim_list)))

print("Stopwords in Gensim not present in the Stones, Dennis, Kwantes:", set(gensim_list) -  set(reference_array))
print("Stopwords not in Gensim:", set(reference_array) -  set(gensim_list))

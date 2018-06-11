import gensim

# Load Google's pre-trained Word2Vec model.
model = gensim.models.KeyedVectors.load_word2vec_format('/home/laurent/Downloads/GoogleNews-vectors-negative300.bin', binary=True)

print model.wv['computer']

print model.wv.similarity('cat', 'dog')
print model.wv.similarity('cat', 'animal')
print model.wv.similarity('cat', 'table')

print model.wv.most_similar_cosmul(positive=['cat'])

print model.wv.most_similar_cosmul(positive=['woman', 'king'], negative=['man'])


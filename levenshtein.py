import Levenshtein


print Levenshtein.distance("chat", "chien")
print Levenshtein.distance("animal", "chien")
print Levenshtein.distance("orthographe", "ortografe")

print Levenshtein.ratio("chat", "chien")
print Levenshtein.ratio("animal", "chien")
print Levenshtein.ratio("orthographe", "ortografe")


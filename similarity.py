import math
# or you can use simpl from "torch.nn.functional import cosine_similarity"
def dot_product(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

def magnitude(vector):
    return math.sqrt(sum(x**2 for x in vector))

def cosine_similarity(vector1, vector2):
    dot_prod = dot_product(vector1, vector2)
    mag1 = magnitude(vector1)
    mag2 = magnitude(vector2)
    return dot_prod / (mag1 * mag2)


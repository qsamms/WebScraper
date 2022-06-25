def reverse(x):
    return x[::-1]

def calculateScore(rating, matches):
    if(rating == 0):
        return matches
    else:
        return rating + matches
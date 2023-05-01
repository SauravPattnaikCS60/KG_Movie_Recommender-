'''

This file performs a limited depth first search to get the recommendations given an user input

'''

def depth_limited_search(recommendation_model, source_movie, limit=2):
    movie_stack = []
    movie_stack.append(source_movie)
    depth = 0
    depth_stack = []
    depth_stack.append(depth)
    recommendations = []

    while (len(movie_stack) != 0):

        movie_popped = movie_stack.pop()
        curr_depth = depth_stack.pop()

        if curr_depth > limit or movie_popped in recommendations:
            continue

        movie_neighbours = [t[0] for t in recommendation_model[movie_popped]]
        depth = curr_depth + 1
        depth_stack = depth_stack + [depth] * len(movie_neighbours)
        movie_stack = movie_stack + movie_neighbours
        recommendations.append(movie_popped)

    recommendations.remove(source_movie)
    return recommendations
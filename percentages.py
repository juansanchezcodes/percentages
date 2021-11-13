def percent_maker(freq_dist):
    counter = 0
    for key in freq_dist:
        counter = counter + freq_dist[key]
        total = counter
        a_dict_percentages = {}
        for key in freq_dist:
            proportion = freq_dist[key] / total
            percentage = proportion * 100
            a_dict_percentages[key] = round(percentage, 2)
    return a_dict_percentages
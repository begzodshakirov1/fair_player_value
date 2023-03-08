import pandas as pd
from itertools import combinations, permutations
import sys

#Reading file from events list
features_list = pd.read_csv('fv_estimates.csv')

def combine_names(pl_name):
    split_name = pl_name.split()
    comb_list = []
    for r in range(1, len(split_name)+1):
        for comb in permutations(split_name, r):
            comb_list.append(" ".join(comb))
    return comb_list

test_comb = [combine_names(features_list['Player Name'][_]) for _ in range(len(features_list))]

def get_player_names(inputname):
    columns_to_show = ['Player Name', 'Market Value (mln \u20ac)']
    index_list = []
    for j in range(len(test_comb)):
        if inputname.title() in test_comb[j]:
            index_list.append((j))

    return features_list.iloc[index_list][columns_to_show] #\
                    #.style.set_properties(**{'text-align': 'left'}) \
                    #.set_table_styles([dict(selector = 'th', props=[('text-align', 'left')])])

if __name__ == '__main__':
    inputname = sys.argv[1]
    
    print(sys.argv)
    print(get_player_names(inputname))
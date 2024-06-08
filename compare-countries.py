import pandas as pd
import glob
import os


def search_proposals(country, data, col):  # Function to replace countries
    elements = country.split()
    proposals = []
    for j in elements:
        if j != 'and':
            proposals.extend(data[data[col].str.contains(j)][col].values)
    if len(proposals) > 0:
        return proposals
    else:
        return 'No proposals found. You may consider removing this object!'


# import all wh-happiness files and concatenate to one dataframe
path = r'data'
wh_files = glob.glob(os.path.join(path, "wh-*.csv"))
df_from_each_file = (pd.read_csv(f) for f in wh_files)
world_happiness = pd.concat(df_from_each_file, ignore_index=False, keys=['2015', '2016', '2017', '2018', '2019'])

# import countries of the world
countries_of_the_world = pd.read_csv('data/countries of the world.csv')

# merge columns of importance that mean the same
world_happiness['Country'] = world_happiness['Country'].combine_first(world_happiness['Country or region'])
world_happiness['Happiness Score'] = world_happiness['Happiness Score'].combine_first(
    world_happiness['Happiness.Score'])
world_happiness['Happiness Score'] = world_happiness['Happiness Score'].combine_first(world_happiness['Score'])
world_happiness['Happiness Rank'] = world_happiness['Happiness Rank'].combine_first(world_happiness['Happiness.Rank'])
world_happiness['Happiness Rank'] = world_happiness['Happiness Rank'].combine_first(world_happiness['Overall rank'])

# remove country duplicates and sort alphabetically
countries_wh = world_happiness.copy()
countries_wh = countries_wh.drop_duplicates(subset='Country')
countries_wh.reset_index(inplace=True, drop=True)
countries_wh.sort_values(by='Country', inplace=True)

# remove white space at the end of all countries for easier comparison and sort alphabetically
countries_of_the_world['Country'] = countries_of_the_world['Country'].str[:-1]
countries_of_the_world.sort_values(by='Country', inplace=True)

# compare and rename or remove differently named countries
for i in countries_wh['Country']:
    if i not in countries_of_the_world['Country'].values:
        print('The country', i, ' may be spelled wrong. I found the following proposals: ',
              search_proposals(i, countries_of_the_world, 'Country'))
        action = str(input(
            'Do you wish to replace or remove this country? Type the new name for replacement, or "r" for removal:'))
        if action == 'r':
            world_happiness.drop(world_happiness[world_happiness['Country'] == i].index, inplace=True)
        else:
            world_happiness['Country'] = world_happiness['Country'].replace({i: action})

# Create new csv files with new names and equal number of columns
world_happiness.loc['2015'].to_csv('wh-2015_new.csv', index=False)
world_happiness.loc['2016'].to_csv('wh-2016_new.csv', index=False)
world_happiness.loc['2017'].to_csv('wh-2017_new.csv', index=False)
world_happiness.loc['2018'].to_csv('wh-2018_new.csv', index=False)
world_happiness.loc['2019'].to_csv('wh-2019_new.csv', index=False)


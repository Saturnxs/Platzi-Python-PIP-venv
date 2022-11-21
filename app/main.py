import utils # Importing the `utils` module.
#import handle_csv
import charts
import pandas as pd

def run():
    
    '''
    data = list(filter(lambda item: item['Continent'] == 'South America', data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    '''
    
    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'Africa']
    
    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    
    charts.generate_pie_chart(countries, percentages, 'SouthAmericaPopulation')
    
    
    # data = handle_csv.read_csv('data.csv')
    country = input('Type country: ')
    result = utils.population_by_country(df, country)
    
    
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values, country['Country/Territory'])
        charts.generate_pie_chart(labels, values, country['Country/Territory'])
        
           

if __name__ == "__main__":
    run()
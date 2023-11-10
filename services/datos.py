import pandas as pd

def transform():
    df1 = pd.read_csv("data/2015.csv", index_col=0)
    df2 = pd.read_csv("data/2016.csv", index_col=0)
    df3 = pd.read_csv("data/2017.csv", index_col=0)
    df4 = pd.read_csv("data/2018.csv", index_col=0)
    df5 = pd.read_csv("data/2019.csv", index_col=0)

    ### DF1
    df1 = df1.drop(['Standard Error','Region'], axis = 1)
    df1['Year'] = 2015

    ### DF2
    df2 = df2.drop(["Lower Confidence Interval","Upper Confidence Interval","Region"], axis = 1)
    df2['Year'] = 2016

    ### DF3
    df3 = df3.drop(["Whisker.high","Whisker.low"],axis =1)
    df3['Year'] = 2017
    df3 = df3.rename(columns={'Happiness.Rank': 'Happiness Rank', 'Happiness.Score': 'Happiness Score', 'Economy..GDP.per.Capita.':'Economy (GDP per Capita)','Health..Life.Expectancy.':'Health (Life Expectancy)','Trust..Government.Corruption.':'Trust (Government Corruption)','Dystopia.Residual':'Dystopia Residual'})

    ### DF4
    df4['Year'] = 2018
    df4['Happiness Rank'] = df4.index
    df4 = df4.rename(columns={'Country or region':'Country', 'Score': 'Happiness Score','Social support':'Family', 'GDP per capita':'Economy (GDP per Capita)','Healthy life expectancy':'Health (Life Expectancy)','Freedom to make life choices':'Freedom','Perceptions of corruption':'Trust (Government Corruption)'})
    df4.set_index('Country', inplace=True)

    ### DF5
    df5["Year"] = 2019
    df5['Happiness Rank'] = df5.index
    df5 = df5.rename(columns={'Country or region':'Country', 'Score': 'Happiness Score','Social support':'Family', 'GDP per capita':'Economy (GDP per Capita)','Healthy life expectancy':'Health (Life Expectancy)','Freedom to make life choices':'Freedom','Perceptions of corruption':'Trust (Government Corruption)'})
    df5.set_index('Country', inplace=True)

    ### Union de los dataframes y transformaciones finales
    dff = pd.concat([df1, df2, df3, df4, df5], ignore_index=False)
    dff = dff.drop(["Dystopia Residual","Happiness Rank","Trust (Government Corruption)","Generosity","Year"], axis = 1)
    dff['Happiness Score'] = dff['Happiness Score'].round(3)
    dff['Family'] = dff['Family'].round(3)
    dff['Economy (GDP per Capita)'] = dff['Economy (GDP per Capita)'].round(3)
    dff['Health (Life Expectancy)'] = dff['Health (Life Expectancy)'].round(3)
    dff['Freedom'] = dff['Freedom'].round(3)
    dff = dff.dropna()
    dff = dff.sample(frac=0.3, random_state=12)
    dff.to_csv("data/resultados.csv")
    return dff
    





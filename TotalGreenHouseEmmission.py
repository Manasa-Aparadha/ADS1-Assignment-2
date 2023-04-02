# Libraries to be used
import pandas as pd


# FUNCTION THAT WILL RETURN TWO ARGUMENTS: YEARS AS COLUMNS AND COUNTRIES AS COLUMNS
def process_co2_data(filename):
    # Load the data into a DataFrame
    df = pd.read_csv(filename, skiprows=4)
    
    # Extract the data for the years 2010-2019
    yearsDF = df.loc[:, 'Country Name':'2019']
    yearsDF.columns = [col if not col.isdigit() else str(col) for col in yearsDF.columns]
    
    # Transpose the DataFrame to get a country-centric view
    countriesDF = yearsDF.transpose()
    
    # Replace empty values with 0
    countriesDF = countriesDF.fillna(0)
    
    # Set the column names for the countries DataFrame
    countriesDF.columns = countriesDF.iloc[0]
    countriesDF = countriesDF.iloc[1:]
    countriesDF.index.name = 'Year'
    
    # Set the column names for the years DataFrame
    yearsDF = yearsDF.rename(columns={'Country Name': 'Year'})
    yearsDF = yearsDF.set_index('Year')
    
    return yearsDF, countriesDF



#calling the function we created above
yearsDF, countriesDF = process_co2_data('API_EN.ATM.GHGT.ZG_DS2_en_csv_v2_5262928.csv')

# MAKING THE COUNTRIES TO BE COLUMNS
countriesDF

# MAKING THE YEARS TO BE COLUMNS
yearsDF

# EXPLORING THE STATISTICAL PROPERTIES OF INDICATORS

countriesDF.describe()

yearsDF.describe()

# Getting the top 10 countries with the highest Total greenhouse gas emissions (% change from 1990) in the year 2012
yearsDF.nlargest(20, '2012')

countriesDF.info()

yearsDF.info()

# LOOKING AT THE CORELATIONS OF THE DATA FRAME
yearsDF.corr()

# A LINE CHART SHOWING THE 7 COUNTRIES
# Importing the necessary libraries
import matplotlib.pyplot as plt

# Reading the CSV file
df = pd.read_csv('API_EN.ATM.GHGT.ZG_DS2_en_csv_v2_5262928.csv', skiprows=4)

# Selecting the columns with the country names and the years 2002 to 2012
columns_to_select = ['Country Name'] + [f"{year}" for year in range(2002, 2013)]
df = df[columns_to_select]

# Filtering the dataframe to only include the 7 countries of your choice
countries_of_interest = ['United States', 'Russian Federation', 'China', 'India', 'Nigeria', 'Brazil', 'Australia']
df = df[df['Country Name'].isin(countries_of_interest)]

# Setting the index of the dataframe to be the 'Country Name' column
df.set_index('Country Name', inplace=True)

# Plotting the line chart
plt.figure(figsize=(10,6))
for country in countries_of_interest:
    plt.plot(df.loc[country], label=country)
plt.legend()
plt.title('Total greenhouse gas emissions (% change from 1990)')
plt.xlabel('Year')
plt.ylabel('% change from 1990')
plt.show()

# PLOTTING A BAR CHART OF Total greenhouse gas emissions (% change from 1990) in 2012
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("API_EN.ATM.GHGT.ZG_DS2_en_csv_v2_5262928.csv", skiprows=4)

# Select the columns for the years 2002 to 2012
cols = df.columns[47:58]

# Select the rows for the countries of your choice
countries = ['United States', 'Russian Federation', 'China', 'India', 'Nigeria', 'Brazil', 'Australia']
df = df[df["Country Name"].isin(countries)]

# Set the index to be the country names
df.set_index("Country Name", inplace=True)

# Transpose the dataframe so that the years become the index and the countries become the columns
df = df[cols].T

# Plot the bar chart
ax = df.plot(kind="bar", figsize=(10, 6))

# Set the title and axis labels
ax.set_title("Total greenhouse gas emissions (% change from 1990) for 7 countries from 2002 to 2012")
ax.set_xlabel("Year")
ax.set_ylabel("Total greenhouse gas emissions (% change from 1990)")

# Show the plot
plt.show()

# PLOTTING A BAR CHART FOR THE GDP (current US$) in 2012 for 7 Countries
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
df = pd.read_csv('GDP_DATA.csv')

# Select the columns of interest
columns_of_interest = ['Country Name', '2012']
df = df[columns_of_interest]

# Select 7 countries of your choice
countries = ['United States', 'Russian Federation', 'China', 'India', 'Nigeria', 'Brazil', 'Australia']
df = df[df['Country Name'].isin(countries)]

# Create the bar chart
fig, ax = plt.subplots(figsize=(10,6))
ax.bar(df['Country Name'], df['2012'])

# Set the chart title and axis labels
ax.set_title('GDP (current US$) in 2012 for 7 Countries')
ax.set_xlabel('Country')
ax.set_ylabel('GDP (current US$)')

# Show the chart
plt.show()

# PLOTTING THE HEATMAP
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("API_EN.ATM.GHGT.ZG_DS2_en_csv_v2_5262928.csv", skiprows=4)

# Define a list of 10 countries of your choice
countries = ['United States', 'Russian Federation', 'China', 'India', 'Nigeria', 'Brazil', 'Australia']

# Filter the data for the 7 countries of your choice and the years 2002-2012
df_filtered = df.loc[df['Country Name'].isin(countries), ['Country Name', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011','2012']]
df_filtered.set_index('Country Name', inplace=True)

# Create a heatmap
plt.figure(figsize=(10, 8))
plt.imshow(df_filtered, cmap='YlOrBr', aspect='auto')
plt.xticks(range(len(df_filtered.columns)), df_filtered.columns)
plt.yticks(range(len(df_filtered.index)), df_filtered.index)
plt.colorbar()
plt.title('Total greenhouse gas emissions (% change from 1990)')
plt.show()



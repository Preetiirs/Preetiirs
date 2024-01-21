# Import required libraries
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
           style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    # TASK 1: Add a dropdown list to enable Launch Site selection
    # The default select value is for ALL sites
    # dcc.Dropdown(id='site-dropdown',...)
    html.H1("Automobile Sales Statistics Dashboard", style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
    # May include style for title
    html.Div([
        # Add a Launch Site Drop-down Input Component
        html.Label("Select Launch Site:"),
        dcc.Dropdown(
            id='site-dropdown',
            options=[
                {'label': 'All Sites', 'value': 'ALL'},
                {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
            ],
            value='ALL',
            searchable=True
        ),
        html.Br(),

        # TASK 2: Add a pie chart to show the total successful launches count for all sites
        # If a specific launch site was selected, show the Success vs. Failed counts for the site
        html.Div(dcc.Graph(id='success-pie-chart')),
        html.Br(),

        html.P("Payload range (Kg):"),
        # TASK 3: Add a slider to select payload range
        dcc.RangeSlider(id='payload-slider',
        min=0, max=10000, step=1000, 
        marks={0: '0',
               10000: '10000'},
        value=[min_payload, max_payload]),

        # TASK 4: Add a scatter chart to show the correlation between payload and launch success
        html.Div(dcc.Graph(id='success-payload-scatter-chart')),
    ])  # Add this closing parenthesis
])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='class', 
        names='Launch Site', 
        title='Sucess ratio for All the launch sites')
        return fig
    elif entered_site == 'CCAFS LC-40':
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        count_class_1 = (filtered_df['class'] == 1).sum()
        count_class_0 = (filtered_df['class'] == 0).sum()
        count_class = [count_class_1,count_class_0]
        class_type = [0,1]
        fig = px.pie( values = count_class, 
        names = class_type,  
        title='Count of Succes Attemps CCAFS LC-40 Launch Site')
        return fig
    elif entered_site == 'CCAFS SLC-40':
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        count_class_1 = (filtered_df['class'] == 1).sum()
        count_class_0 = (filtered_df['class'] == 0).sum()
        count_class = [count_class_1,count_class_0]
        class_type = [0,1]
        fig = px.pie( values = count_class, 
        names = class_type,  
        title='Count of Succes Attemps CCAFS SLC-40 Launch Site')
        return fig
    elif entered_site == 'KSC LC-39A':
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        count_class_1 = (filtered_df['class'] == 1).sum()
        count_class_0 = (filtered_df['class'] == 0).sum()
        count_class = [count_class_1,count_class_0]
        class_type = [0,1]
        fig = px.pie( values = count_class, 
        names = class_type,  
        title='Count of Succes Attemps KSC LC-39A Launch Site')
        return fig
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        count_class_1 = (filtered_df['class'] == 1).sum()
        count_class_0 = (filtered_df['class'] == 0).sum()
        count_class = [count_class_1,count_class_0]
        class_type = [0,1]
        fig = px.pie( values = count_class, 
        names = class_type,  
        title='Count of Succes Attemps of VAFB SLC-4E Launch Site')
        return fig
        # return the outcomes piechart for a selected site
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
[Input(component_id='site-dropdown', component_property='value'), 
Input(component_id="payload-slider", component_property="value")])
def get_scatter_chart(entered_site, payload_range):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', 
        y = 'class', color = 'Booster Version Category',
        title='Correlation between Payload and Sucess for all sites')
        return fig
    elif entered_site == 'CCAFS LC-40':
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', 
        y = 'class', color = 'Booster Version Category',
        title='Correlation between Payload and Sucess for CCAFS LC-40 Launch Site')
        return fig
    elif entered_site == 'CCAFS SLC-40':
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', 
        y = 'class', color = 'Booster Version Category',
        title='Correlation between Payload and Sucess for CCAFS SLC-40 Launch Site')
        return fig
    elif entered_site == 'KSC LC-39A':
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', 
        y = 'class', color = 'Booster Version Category',
        title='Correlation between Payload and Sucess for KSC LC-39A Launch Site')
        return fig
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', 
        y = 'class', color = 'Booster Version Category',
        title='Correlation between Payload and Sucess for VAFB SLC-4E Launch Site')
        return fig
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8052)
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np


with open('response1.json') as f:
    data1 = json.load(f)

labels = [row['ResponsibleGroupName'] for row in data1['DataRows']]
values = [row['CountTicketID'] for row in data1['DataRows']]

fig1 = go.Figure(
    go.Bar(
        x=labels,
        y=values,
        marker=dict(color=['#4C4C4C', '#707070', '#999999', '#C2C2C2'])
    )
)
fig1.update_layout(
    title=data1['Name'],
    xaxis_title='Responsible Group Name',
    yaxis_title='Count Ticket ID'
)

with open('response2.json') as f:
    data2 = json.load(f)

labels = [row['ResponsibleFullName'] for row in data2['DataRows']]
values = [row['CountTicketID'] for row in data2['DataRows']]

fig2 = go.Figure(
    go.Pie(
        labels=labels,
        values=values,
        marker=dict(colors=['#4C4C4C', '#707070', '#999999', '#C2C2C2']),
        textinfo='label+percent'
    )
)
fig2.update_layout(
    title=data2['Name']
)

with open('response3.json') as f:
    data3 = json.load(f)

labels = [row['TypeName'] for row in data3['DataRows']]
values = [row['CountTicketID'] for row in data3['DataRows']]

fig3 = go.Figure(
    go.Pie(
        labels=labels,
        values=values,
        marker=dict(colors=['#4C4C4C', '#707070', '#999999', '#C2C2C2']),
        textinfo='label+percent'
    )
)
fig3.update_layout(
    title=data3['Name']
)

with open('response4.json') as f:
    data4 = json.load(f)

labels = [row['Responsibility'] for row in data4['DataRows']]
values = [row['CountTicketID'] for row in data4['DataRows']]

fig4 = go.Figure(
    go.Pie(
        labels=labels,
        values=values,
        marker=dict(colors=['#4C4C4C', '#707070', '#999999', '#C2C2C2']),
        textinfo='label+percent'
    )
)
fig4.update_layout(
    title=data4['Name']
)

with open('response5.json') as f:
    data5 = json.load(f)

labels = [row['TypeName'] for row in data5['DataRows']]
values = [row['CountTicketID'] for row in data5['DataRows']]

fig5 = go.Figure(
    go.Pie(
        labels=labels,
        values=values,
        marker=dict(colors=['#4C4C4C', '#707070', '#999999', '#C2C2C2']),
        textinfo='label+percent'
    )
)
fig5.update_layout(
    title=data5['Name']
)

app = dash.Dash()

app.layout = html.Div([

    html.Div([
        html.H1('My Dashboard')
    ], style={'textAlign': 'center'}),

    html.Div([
        dcc.Graph(
            id='graph1',
            figure={
                'data': [go.Bar(x=[row['ResponsibleGroupName'] for row in data1['DataRows']],
                                y=[row['CountTicketID'] for row in data1['DataRows']],
                                marker=dict(color=['Cyan', 'darkblue', 'lightseagreen', 'springgreen']))],
                'layout': go.Layout(title=data1['Name'], xaxis_title='Group Name', yaxis_title='Count')
            }
        )
    ], className='six columns'),

    html.Div([
        dcc.Graph(
            id='graph2',
            figure={
                'data': [go.Bar(x=[row['ResponsibleFullName'] for row in data2['DataRows']],
                                y=[row['CountTicketID'] for row in data2['DataRows']],
                                marker=dict(color=['darkblue', 'palegreen', 'limegreen', 'aquamarine']))],
                'layout': go.Layout(title=data2['Name'], xaxis_title='Full Name', yaxis_title='Count')
            }
        )
    ], className='six columns'),

    html.Div([
        dcc.Graph(
            id='graph3',
            figure={
                'data': [go.Pie(labels=[row['TypeName'] for row in data3['DataRows']],
                                values=[row['CountTicketID'] for row in data3['DataRows']],
                                marker=dict(colors=['Cyan', 'darkblue', 'lightseagreen', 'springgreen']))],
                'layout': go.Layout(title=data3['Name'])
            }
        )
    ], className='six columns'),

    html.Div([
        dcc.Graph(
            id='graph4',
            figure={
                'data': [go.Pie(labels=[row['Responsibility'] for row in data4['DataRows']],
                                values=[row['CountTicketID'] for row in data4['DataRows']],
                                marker=dict(colors=['Cyan', 'darkblue', 'lightseagreen', 'springgreen']))],
                'layout': go.Layout(title=data4['Name'])
            }
        )
    ], className='six columns'),

   ])
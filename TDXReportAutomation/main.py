import json
import plotly.graph_objs as go
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from collections import defaultdict
from dateutil import parser

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
fig = go.Figure()



# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '5%',
    'margin-right': '5%',
    'padding': '20px 10p',

}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#42275a'
}

controls = dbc.FormGroup(
    [
        html.P('Dropdown', style={
            'textAlign': 'center'
        }),
        dcc.Dropdown(
            id='dropdown',
            options=[{
                'label': 'Value One',
                'value': 'value1'
            }, {
                'label': 'Value Two',
                'value': 'value2'
            },
                {
                    'label': 'Value Three',
                    'value': 'value3'
                }
            ],
            value=['value1'],  # default value
            multi=True
        ),
        html.Br(),
        html.P('Range Slider', style={
            'textAlign': 'center'
        }),
        dcc.RangeSlider(
            id='range_slider',
            min=0,
            max=20,
            step=0.5,
            value=[5, 15]
        ),
        html.P('Check Box', style={
            'textAlign': 'center'
        }),
        dbc.Card([dbc.Checklist(
            id='check_list',
            options=[{
                'label': 'Value One',
                'value': 'value1'
            },
                {
                    'label': 'Value Two',
                    'value': 'value2'
                },
                {
                    'label': 'Value Three',
                    'value': 'value3'
                }
            ],
            value=['value1', 'value2'],
            inline=True
        )]),
        html.Br(),
        html.P('Radio Items', style={
            'textAlign': 'center'
        }),
        dbc.Card([dbc.RadioItems(
            id='radio_items',
            options=[{
                'label': 'Value One',
                'value': 'value1'
            },
                {
                    'label': 'Value Two',
                    'value': 'value2'
                },
                {
                    'label': 'Value Three',
                    'value': 'value3'
                }
            ],
            value='value1',
            style={
                'margin': 'auto'
            }
        )]),
        html.Br(),
        dbc.Button(
            id='submit_button',
            n_clicks=0,
            children='Submit',
            color='primary',
            block=True
        ),
    ]
)



# Load the JSON files
with open('response1.json') as f:
    data1 = json.load(f)
with open('response2.json') as f:
    data2 = json.load(f)
with open('response3.json') as f:
    data3 = json.load(f)
with open('response4.json') as f:
    data4 = json.load(f)
with open('response5.json') as f:
    data5 = json.load(f)
with open('response6.json') as f:
    data6 = json.load(f)
with open('response7.json') as f:
    data7 = json.load(f)
with open('response8.json') as f:
    data8 = json.load(f)
with open('response9.json') as f:
    data9 = json.load(f)
with open('open3d.json') as f:
    open3d = json.load(f)
with open('open7d.json') as f:
    open7d = json.load(f)
with open('open14d.json') as f:
    open14d = json.load(f)
with open('createtoclose.json') as f:
    createtoclose = json.load(f)
with open('resolvedweek') as f:
    resolvedweek = json.load(f)
# Created vs Resolved calculation #################
resolved_tickets = {row['ResponsibleFullName']: row['CountTicketID'] for row in data2['DataRows']}
created_tickets = {row['ResponsibleFullName']: row['CountTicketID'] for row in data9['DataRows']}

data2_percent = []
for name, count in resolved_tickets.items():
    if name in created_tickets:
        resolved_percent = count / created_tickets[name] * 100
        data2_percent.append({'ResponsibleFullName': name, 'PercentResolved': resolved_percent})


#Merge json files for open tickets report
json_data = [open3d, open7d, open14d]
# Merge 3d 7d 14d into a grouped bar chart#################################################
data_dict = {}
for data in json_data:
    for row in data['DataRows']:
        name = row['ResponsibleFullName']
        count = row['CountTicketID']
        if name not in data_dict:
            data_dict[name] = [count]
        else:
            data_dict[name].append(count)

# Create the grouped bar chart
data = []
for name, counts in data_dict.items():
    data.append(go.Bar(name=name, x=['Open Tickets 3d', 'Open Tickets 7d', 'Open Tickets 14d', ], y=counts))

fig = go.Figure(data=data)
fig.update_layout(barmode='group', title='Open Tickets 3d/7d/14d', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

# Compute handling time for each technician
#technicians = defaultdict(list)
#for row in createtoclose["DataRows"]:
#    name = row["ResponsibleFullName"]
#    created = parser.parse(row["CreatedDate"])
#    closed = parser.parse(row["ClosedDate"])
#    handling_time = (closed - created).total_seconds() / 3600
#    technicians[name].append(handling_time)

# Compute total average handling time for each technician
#averages = {}
#for name, times in technicians.items():
#    averages[name] = sum(times) / len(times)





content_first_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(
                id='Average Handling Time By Tech',
                figure={
                    'data': [
                        go.Bar(
                            x=[row['ResponsibleFullName'] for row in data2['DataRows']],
                            y=[row['MetCreateToResolveAbsolute'] for row in data2['DataRows']],
                            marker=dict(color=['Cyan', 'darkblue', 'lightseagreen', 'springgreen', 'Cyan', 'darkblue', 'lightseagreen', 'springgreen', 'Cyan', 'darkblue', 'lightseagreen', 'springgreen'])
                        )
                    ],
                    'layout': go.Layout(
                        title='Average Handling Time By Tech YTD',
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        margin=dict(l=50, r=50, t=50, b=80)
                    )
                }
            ),
            style={'width': '30vh', 'height': '20vh', 'display': 'inline-block'}
        ),




        dbc.Col(
            dcc.Graph(id='Wifi and Networking - Ticket Count By Year',
            figure={
                'data': [go.Bar(x=[row['Name'] for row in [data5, data7]],
                                y=[sum([d['CountTicketID'] for d in row['DataRows']]) for row in [data5, data7]],
                                marker=dict(color=['darkblue', 'palegreen']))],
                'layout': go.Layout(title='WiFi & Networking Tickets by Year',  paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=25, r=25, t=25, b=25))}), style={'width': '30vh', 'height': '20vh', 'display': 'inline-block'}
        ),

        dbc.Col(
            dcc.Graph(
                id='Help Desk Escalated Ticket Volume by Group, 2022',
                figure={
                    'data': [go.Bar(x=[row['ResponsibleGroupName'] for row in data1['DataRows']],
                                    y=[row['CountTicketID'] for row in data1['DataRows']],
                                    marker=dict(color=['Cyan', 'darkblue', 'lightseagreen', 'springgreen', 'Cyan', 'darkblue', 'lightseagreen', 'springgreen', 'Cyan', 'darkblue', 'lightseagreen', 'springgreen']))],
                    'layout': go.Layout(title=data1['Name'], paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=25, r=25, t=60, b=80))}, style={'width': '45vh', 'height': '30vh', 'display': 'inline-block'}

            ))
    ]
)

content_second_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='Currently Assigned',
            figure={
                'data': [go.Pie(labels=[row['Responsibility'] for row in data4['DataRows']],
                         values=[row['CountTicketID'] for row in data4['DataRows']],
                         textinfo='value',
                         marker=dict(colors=['Cyan', 'darkblue', 'lightseagreen', 'springgreen']))],
             'layout': go.Layout(title=data4['Name'], paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=25, r=25, t=55, b=25))}), md=4, style={'width': '45vh', 'height': '30vh', 'display': 'inline-block'}
        ),
        dbc.Col(
            dcc.Graph(id='Weekly Ticket Volume By Type',
            figure={
                'data': [go.Pie(labels=[row['TypeName'] for row in data3['DataRows']],
                             values=[row['CountTicketID'] for row in data3['DataRows']],
                             textinfo='percent',
                             marker=dict(colors=['Cyan', 'darkblue', 'lightseagreen', 'springgreen']))],
             'layout': go.Layout(title=data3['Name'], paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=25, r=25, t=55, b=25))}),
                                style={'width': '45vh', 'height': '30vh', 'display': 'inline-block'}, md=4
        ),
        dbc.Col(
            dcc.Graph(id='Open Tickets 3d/7d/14d', figure=fig, responsive=True, style={'width': '45vh', 'height': '30vh'}),

        )

    ]
)

content_third_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(
                id='Help Desk Tickets Resolved - YTD',
                figure={
                    'data': [go.Bar(
                        x=[row['ResponsibleFullName'] for row in data2_percent],
                        y=[row['PercentResolved'] for row in data2_percent],
                        marker=dict(color=['Cyan', 'darkblue', 'lightseagreen', 'springgreen', 'Cyan', 'darkblue', 'lightseagreen', 'springgreen', 'Cyan', 'darkblue', 'lightseagreen', 'springgreen']),
                        text=[f"{row['PercentResolved']:.2f}%" for row in data2_percent],
                        textposition='auto',
                    )],
                    'layout': go.Layout(title=data2['Name'], paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=25, r=25, t=25, b=25))
                }
            ))
])













#            dcc.Graph(
#                id='handling-time-graph',
#                figure={
#                    'data': [go.Bar(x=list(averages.keys()),
#                                    y=list(averages.values()),
#                                    marker=dict(color=['Cyan', 'darkblue', 'lightseagreen', 'springgreen', 'Cyan', 'darkblue', 'lightseagreen', 'springgreen', 'Cyan', 'darkblue', 'lightseagreen', 'springgreen']))],
#                    'layout': go.Layout(title='Average Handling Time', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=25, r=25, t=60, b=80))}, style={'width': '45vh', 'height': '30vh', 'display': 'inline-block' }#
#
 #           )
 #       ),
 #   ]
#)

#    [
#        dbc.Col(
#            dcc.Graph(
#                id='resolvedweek'
#                figure={
#                    'data': [go.Bar(x=[row['ResponsibleFullName'] for row in resolvedweek],
#                                y=[row['CountTicketID'] for row in data2_percent]},
#                                marker=dict(color=['darkblue', 'palegreen', 'limegreen', 'aquamarine', 'Cyan', 'darkblue', 'lightseagreen', 'springgreen']),
#}
#            )
#)







content = html.Div(
    [
        html.H2('HelpDesk TDX Metrics Dashboard', style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        content_second_row,
        content_third_row,
    ],
    style=CONTENT_STYLE
)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], title="SA Heldesk Metrics")
app.layout = html.Div(
    style={
        "background": "linear-gradient(to bottom right, white, orange)",
        "height": "100vh"
    },
    children=[content]
)


if __name__ == '__main__':
   app.run_server(debug=True)

  # dbc.Col(
  ##     dcc.Graph(
   #        id='Help Desk Tickets Created vs. Resolved',
   #        figure={
   #            'data': [go.Bar(x=[row['ResponsibleFullName'] for row in data2_percent],
   #                            y=[row['PercentResolved'] for row in data2_percent],
   #                            marker=dict(
   #                                color=['darkblue', 'palegreen', 'limegreen', 'aquamarine', 'Cyan', 'darkblue',
   #                                       'lightseagreen', 'springgreen']),
   #                            text=[f"{row['PercentResolved']:.2f}%" for row in data2_percent],
   #                            textposition='auto',
   #                            )],
   #            'layout': go.Layout(title='Help Desk Tickets Created vs. Resolved, YTD', paper_bgcolor='rgba(0,0,0,0)',
   #                                plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=25, r=25, t=60, b=80))},
   #        style={'width': '45vh', 'height': '30vh', 'display': 'inline-block'}#

   #    )),
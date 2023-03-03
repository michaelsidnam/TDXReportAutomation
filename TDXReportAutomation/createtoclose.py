import json
from dateutil import parser
from collections import defaultdict

with open("createtoclose2.json", "r") as f:
    createtoclose = json.load(f)

# Compute handling time for each technician
technicians = defaultdict(list)
for row in createtoclose["DataRows"]:
    name = row["ResponsibleFullName"]
    created = parser.parse(row["CreatedDate"])
    closed = parser.parse(row["ClosedDate"])
    handling_time = (closed - created).total_seconds() / 3600
    technicians[name].append(handling_time)

# Compute total average handling time for each technician
averages = {}
for name, times in technicians.items():
    averages[name] = sum(times) / len(times)

# Plot the results using Plotly Dash
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="Average Handling Time by Technician"),
    dcc.Graph(
        id="handling-time-graph",
        figure={
            "data": [
                {
                    "x": list(averages.keys()),
                    "y": list(averages.values()),
                    "type": "bar",
                    "name": "Average Handling Time (hours)"
                }
            ],
            "layout": {
                "title": "Average Handling Time by Technician",
                "xaxis": {"title": "Technician"},
                "yaxis": {"title": "Average Handling Time (hours)"}
            }
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)

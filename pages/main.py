import dash
from dash import html, dcc
from components import analytic_card, card

dash.register_page(__name__, path='/')


# html.Img(
#     className="navbar__time--icon",
#     src="assets/clock.svg",
# )

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=[1, 2, 3, 4], 
        y=[0, 2, 3, 5], 
        fill='tozeroy',
        marker_color='#a16eff',
        mode='lines'
    )
)
fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    
    margin={"t": 0, "b": 0, "r": 0, "l": 0, "pad": 0},
    xaxis=dict(
        showgrid=False,
        showticklabels=False
    ),
    yaxis=dict(
        showgrid=False,
        showticklabels=False,
        zeroline=False
    )
)

layout = html.Div(
    className="main",
    children=[
        # First row, dropdowns!
        html.Div(
            className="main__dropdown--container main__year",
            children=[
                html.Span("Year:"),
                dcc.Dropdown(
                    options=[1920, 2002, 2003],
                    value=1920,
                    searchable=False,
                    clearable=False
                )
            ]
        ),
        html.Div(
            className="main__dropdown--container main__last",
            children=[
                html.Span("Last:"),
                dcc.Dropdown(
                    options=['Day', 'Week', 'Month', 'Year'],
                    value='Day',
                    searchable=False,
                    clearable=False
                )
            ]
        ),
        # Second Row
        analytic_card(
            class_name="main__sales",
            name="Sales",
        ),
        analytic_card(
            class_name="main__profit",
            name="Profit",
        ),
        analytic_card(
            class_name="main__consumption",
            name="Consumption",
        ),
        # Third Row
        card(
            className="main__revenue-cost",
            children=dcc.Graph(
                className="fill-parent-div analytic-card__graph",
                responsive=True, 
                config={
                    'displayModeBar':False
                },
                figure=fig
            )
        ),
        # Fourth Row
        analytic_card(
            class_name="main__stores",
            name="Stores",
        ),
        analytic_card(
            class_name="main__vendors",
            name="Vendors",
        )
        # Fifth Row
    ]
)

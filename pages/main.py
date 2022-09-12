import dash
from dash import html, dcc


dash.register_page(__name__, path='/')

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

        # Third Row

        # Fourth Row
    ]
)

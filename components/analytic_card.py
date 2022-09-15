from dash import html, dcc
from dash import Input, Output, ALL, State, MATCH, ctx
import dash
import uuid
import plotly.graph_objects as go
from components import card


def analytic_card(class_name, name, df=None):
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
    return card(
        className="analytic-card" if not class_name else "analytic-card " + class_name,
        children=[
            html.Span(
                className="analytic-card__name",
                children=name
            ),
            html.Span(
                className="analytic-card__amount",
                children="18,534$"
            ),
            html.Div(
                className="analytic-card__progress",
                children="^ 3%"
            ),
            dcc.Graph(
                className="fill-parent-div analytic-card__graph",
                responsive=True, 
                config={
                    'displayModeBar':False
                },
                figure=fig
            )
        ]
    )
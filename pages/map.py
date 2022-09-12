import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(
    className="map",
    style={"background-color":"blue"}
)
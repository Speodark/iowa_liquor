import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(
    className="sales",
    style={"background-color":"red"}
)
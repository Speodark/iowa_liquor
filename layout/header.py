from dash import html, dcc
import dash
from dash import Input, Output, State


def header():
    return html.Header(
        className="full-width",
        children=html.Div(
            className="header",
            children=[
                html.Div(
                    className="header__container",
                    children=[
                        html.Div(
                            className="header__menu",
                            children=[
                                # The menu button
                                html.Div(
                                    id = "page-menu",
                                    className="header__menu--button",
                                    children=html.Span(className="icon")
                                ),
                                # App Name
                                html.Span(
                                    children="Iowa Liquor Sales",
                                    className="header__menu--title"
                                )
                            ]
                        ),
                        
                    ]
                ),
                html.Div(
                    className="header__container",
                    children=[
                        # Email
                        html.Div(
                            className="header__mail-container",
                            children=[
                                html.I(
                                    className="gg-mail"
                                ),
                                html.Span(
                                    children="matanmor9@gmail.com",
                                    className="header__mail-container--text"
                                )
                            ]
                        ),

                        # Avatar
                        html.Div(
                            className="header__user-container",
                            children=[
                                html.Img(
                                    src="user_pictures/matan_face.jpg",
                                    alt="Avatar",
                                    className="header__user-container--avatar"
                                ),
                                html.Span(
                                    children="Matan Morduch",
                                    className="header__user-container--text"
                                )
                            ]
                        ),
                        
                    ]
                )
            ]
        )
    )



@dash.callback(
    Output("page-menu", "className"),
    Input("page-menu", "n_clicks"),
    State("page-menu", "className"),
    prevent_initial_call=True
)
def open_menu(_, class_name):
    if "clicked" in class_name:
        return class_name.replace(" clicked","")
    else:
        return class_name + " clicked"
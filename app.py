from whitenoise import WhiteNoise
import dash
from dash import html, dcc
from layout import header

# initilaize the app
app = dash.Dash(
    __name__, 
    suppress_callback_exceptions=True,
    use_pages=True
)


# Generate the app layout
def layout():
    return html.Div(
        className="container",
        children=[

            dcc.Location(id='url', refresh=False),

            header(),
            
            html.Div(
                className='layout',
                children=dash.page_container
            ),
        ]
    )


# For the heroku deployment
server = app.server
# set the static folder
server.wsgi_app = WhiteNoise(server.wsgi_app, root='assets/')
# title
app.title = 'Animal Shelter'
# set the layout
app.layout = layout
# start the app
if __name__ == "__main__":
    app.run_server(debug=True, port=5050, host="0.0.0.0")
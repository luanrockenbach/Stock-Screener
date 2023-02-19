import yfinance
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc


ticket = input(str("\n - Digite qual ação você gostaria de analisar: "))


def show_dashboard(filtered_stocks):
    # criar um gráfico de dispersão com as ações filtradas

    app = Dash(__name__, title='Djin', )

    fig = px.line(filtered_stocks, x='Date', y='Open', template='plotly_dark', title=str(ticket))

    app.layout = html.Div(children=[
        html.H1(children='Djin', style={'textAlign': 'center', 'color': 'blue', 'fontSize': 50}),

        html.Div(children='''
            Dash: A web application framework for your data.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

    if __name__ == '__main__':
        app.run_server(debug=True)


def get_stock(ticker):
    ticker = yfinance.Ticker(ticket+".SA")

    stock_data = pd.DataFrame(ticker.history(period="1mo", interval="1d"))
    stock_data.reset_index(inplace=True)
    return stock_data


show_dashboard(get_stock(ticket))

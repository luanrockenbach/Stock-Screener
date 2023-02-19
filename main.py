import yfinance
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc


def show_dashboard(filtered_stocks):
    # criar um gráfico de dispersão com as ações filtradas

    app = Dash(__name__)

    fig = px.line(filtered_stocks, x='Date', y='Open')

    app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

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


ticket = input(str("\n - Digite qual ação você gostaria de analisar: "))
ticker = yfinance.Ticker(ticket+".SA")

stock_data = pd.DataFrame(ticker.history(period="1mo", interval="1d"))
stock_data.reset_index(inplace=True)
show_dashboard(stock_data)

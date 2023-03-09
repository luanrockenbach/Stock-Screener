import yfinance
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import fundamentus

ticker_list = fundamentus.list_papel_all()
result_df = pd.DataFrame()


def get_stock(ticker):
    global result_df
    if ticker.upper() in ticker_list:
        result_df = pd.DataFrame(fundamentus.get_papel(ticker))
        result_df.reset_index(inplace=True)

    ticker = ticker + '.SA'
    stock_data = pd.DataFrame(yfinance.Ticker(ticker).history(period="5y", interval="1d"))
    stock_data.reset_index(inplace=True)
    return stock_data


# fig = px.line(get_stock('B3SA3'), x='Date', y='Open', template='plotly_dark', title=str('B3SA3'))

stock_df = get_stock('B3SA3')
fig = go.Figure(data=[go.Candlestick(x=stock_df['Date'],
                                     open=stock_df['Open'], high=stock_df['High'],
                                     low=stock_df['Low'], close=stock_df['Close'],
                                     increasing_line_color='#29f740',
                                     decreasing_line_color='#fa461f')])

fig.update_layout(paper_bgcolor="gray", plot_bgcolor='black', margin=dict(
    l=0,  # left margin
    r=0,  # right margin
    b=0,  # bottom margin
    t=0  # top margin
))
fig.update_xaxes(rangeslider_visible=False)

app = Dash(__name__, title='Djin')

app.layout = html.Div(className="app-header", children=[

    html.Div(className='title', children=[

        html.H1(className='page-title', children='Djin'),
        html.H2(className='sub-title', children="Djin: Criado por Luan Rockenbach\n"),
    ]),

    html.Div(className='search-bar-div', children=[dcc.Input(className='search-bar', id="input_search", type="text",
                                                             placeholder="Digite uma empresa")]),

    dcc.Graph(
        id='price-graph',
        figure=fig,
        config={'displayModeBar': False}
    ),

    html.Div(id='results', className='Stock-data', children=[
        html.Div(className='pl', children=result_df['PL']),
    ])

])


@app.callback(
    Output('price-graph', 'figure'),
    Input('input_search', 'value'),
    suppress_callback_exceptions=True
)
def update_output(value):
    global ticker_list
    global fig
    global stock_df
    try:
        if value.upper() in ticker_list:
            stock_df = get_stock(value.upper())
            fig = go.Figure(data=[go.Candlestick(x=stock_df['Date'],
                                                 open=stock_df['Open'], high=stock_df['High'],
                                                 low=stock_df['Low'], close=stock_df['Close'],
                                                 increasing_line_color='#29f740',
                                                 decreasing_line_color='#fa461f')])
            fig.update_layout(paper_bgcolor="gray", plot_bgcolor='black', margin=dict(
                l=0,  # left margin
                r=0,  # right margin
                b=0,  # bottom margin
                t=0  # top margin
            ))
            fig.update_xaxes(rangeslider_visible=False)
        else:
            print("\nNada a ver")
    except AttributeError:
        pass
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

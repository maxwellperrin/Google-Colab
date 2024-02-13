from dash import Dash, html, dcc, Input, Output, dash_table, callback
import plotly.express as px
import pandas as pd



# Création de l'application
app = Dash(__name__)

# Exemple de données
#df = pd.DataFrame({
    #'x': [1, 2, 3, 4, 5],
    #'y': [10, 11, 12, 13, 14]
#})

# Définition du layout avec un Slider
#app.layout = html.Div([
    #html.H1("Dashboard avec Dash"),
    #dcc.Graph(id='line-graph'),
    #dcc.Slider(
        #id='slider',
        #min=df['x'].min(),
        #max=df['x'].max(),
        #value=2,  # valeur initiale
        #marks={str(num): str(num) for num in df['x']},
        #step=None
    #)
#])

# Callback pour mettre à jour le graphique
#@app.callback(
    #Output('line-graph', 'figure'),
    #[Input('slider', 'value')]
#)
#def update_graph(slider_value):
    # Filtrer les données en fonction du curseur
    #filtered_df = df[df['x'] <= slider_value]
    #fig = px.line(filtered_df, x='x', y='y', title='Graphique Simple')
    #return fig


df2 = pd.read_csv('https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv', nrows= 10)




# App layout
app.layout = html.Div([
    html.Div(children='Titre de livre'),
    dash_table.DataTable(data=df2.to_dict('records')),
    dcc.Graph(figure = px.histogram(df2, x = df2['title'], y = df2['  num_pages'])),
    dcc.Input(id='input-exemple', type='text', value='Texte initial'),
    dcc.Slider(min=0, max=6500, step=500, value=5)
    
])


#def update_graph(col_chosen):
    #fig = px.histogram(df2, x =df2['title'], y=df2['  num_pages'], title = 'Livre')
    #return fig



# Run the app
if __name__ == '__main__':
    app.run(debug=True)

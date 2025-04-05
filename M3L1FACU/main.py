from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    {
        "fact": "Godzilla es un monstruo ficticio japonés que aparece en películas producidas por Toho Company.",
        "image": "https://img.redbull.com/images/c_crop,x_599,y_0,h_721,w_577/c_fill,w_450,h_600/q_auto:low,f_auto/redbullcom/2019/06/03/ba74340d-e30f-4d60-892d-bf54cf8ea51f/godzilla-2"
    },
    {
        "fact": "El primer Godzilla, llamado 'Gojira', apareció en la película de 1954, dirigida por Ishirô Honda.",
        "image": "https://img.redbull.com/images/c_crop,x_599,y_0,h_721,w_577/c_fill,w_450,h_600/q_auto:low,f_auto/redbullcom/2019/06/03/ba74340d-e30f-4d60-892d-bf54cf8ea51f/godzilla-2"
    },
    
    {
        "fact": "Godzilla es conocido por su gran tamaño y su capacidad para destruir ciudades con su aliento atómico.",
        "image": "https://img.redbull.com/images/c_crop,x_599,y_0,h_721,w_577/c_fill,w_450,h_600/q_auto:low,f_auto/redbullcom/2019/06/03/ba74340d-e30f-4d60-892d-bf54cf8ea51f/godzilla-2"
    },
    
    {
        "fact": "Godzilla ha aparecido en más de 30 películas, convirtiéndose en uno de los íconos más grandes del cine de monstruos.",
        "image": "https://img.redbull.com/images/c_crop,x_599,y_0,h_721,w_577/c_fill,w_450,h_600/q_auto:low,f_auto/redbullcom/2019/06/03/ba74340d-e30f-4d60-892d-bf54cf8ea51f/godzilla-2"
    },

    
    {
        "fact": "El rugido de Godzilla fue creado combinando sonidos de animales reales, como leones, elefantes y ballenas.",
       "image": "https://img.redbull.com/images/c_crop,x_599,y_0,h_721,w_577/c_fill,w_450,h_600/q_auto:low,f_auto/redbullcom/2019/06/03/ba74340d-e30f-4d60-892d-bf54cf8ea51f/godzilla-2"
    },
    
    {
        "fact": "A lo largo de los años, Godzilla ha luchado contra otros monstruos como King Kong, Mothra y Ghidorah.",
        "image": "https://img.redbull.com/images/c_crop,x_599,y_0,h_721,w_577/c_fill,w_450,h_600/q_auto:low,f_auto/redbullcom/2019/06/03/ba74340d-e30f-4d60-892d-bf54cf8ea51f/godzilla-2"
    },
    
]

@app.route("/random_fact")
def datos():
    fact = random.choice(facts_list)
    
    return f'''
        <h1>DATOS CURIOSOS SOBRE GODZILLA</h1>
        <p>{fact["fact"]}</p>
        <img src="{fact["image"]}" alt="Imagen de Godzilla" style="width:50%; max-width:300px;">
        <br>
        <a href="/">Volver</a>
    '''

@app.route("/")
def index():
    return '''
        <h1>Curiosidades sobre Godzilla</h1>
        <a href="/random_fact">¡Ver un dato curioso aleatorio sobre Godzilla!</a>
    '''

if __name__ == "__main__":
    app.run(debug=True)
# El código crea una aplicación web con Flask que muestra datos curiosos sobre Godzilla.
# Se utiliza la biblioteca random para seleccionar un dato curioso aleatorio de una lista predefinida.
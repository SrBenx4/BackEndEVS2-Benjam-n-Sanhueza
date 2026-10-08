from django.shortcuts import render


def inicio(request):

    generos = [
        {
            "nombre": "Acción",
            "descripcion": "Películas llenas de adrenalina y combate."
        },
        {
            "nombre": "Terror",
            "descripcion": "Películas de suspenso y miedo."
        }
    ]

    return render(request, "inicio.html", {"generos": generos})


def accion(request):

    peliculas = [
        {
            "nombre": "Batman",
            "edad": "+13",
            "imagen": "images/Batman.jpg"
        },
        {
            "nombre": "Matrix",
            "edad": "+14",
            "imagen": "images/Matrix.jpg"
        }
    ]

    return render(request, "accion.html", {"peliculas": peliculas})


def terror(request):

    peliculas = [
        {
            "nombre": "Five Nights at Freddy's",
            "edad": "+14",
            "imagen": "images/fnaf.jpg"
        },
        {
            "nombre": "Five Nights at Freddy's 2",
            "edad": "+16",
            "imagen": "images/fnaf2.jpg"
        }
    ]

    return render(request, "terror.html", {"peliculas": peliculas})
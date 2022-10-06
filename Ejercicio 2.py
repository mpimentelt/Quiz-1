#===================================================
# Nombre del Estudiante: Mariana Pimentel
# Carnet: 20221110154
#===================================================
anime = {
    "Demon Slayer": {
        "Temporada 1": [
        {
            "cap": 1,
            "name": "Crueldad",
            "duration": "23:39"
        },
        {
            "cap": 4,
            "name": "Selección final",
            "duration": "23:40"
        },
        {
            "cap": 19,
            "name": "Dios del fuego",
            "duration": "23:40"
        },
        {
            "cap": 26,
            "name": "Una nueva misión",
            "duration": "24:10"
        }
    ],
        "Temporada 2": [
        {
            "cap": 26,
            "name": "Un sueño profundo",
            "duration": "22:55"
        },
        {
            "cap": 43,
            "name": "¡No me rendiré!",
            "duration": "23:40"
        }
    ]
 
        },
    "Spy × Family": {
       
        "Temporada 1":[
        {
            "cap": 4,
            "name": "Objetivo: pasar la entrevista",
            "duration": "24:10"
        },
        {
            "cap": 7,
            "name": "El segundo hijo del objetivo",
            "duration": "24:10"
        }
    ]
    },
    "Attack on Titan": {
        "Temporada 3": [
            {
                "cap": 46,
                "name": "La reina de la muralla",
                "duration": "23:55"
            },
            {
                "cap": 54,
                "name": "Héroe",
                "duration": "23:55"
            }
    ],
        "Temporada 4":[
            {
                "cap": 60,
                "name": "Al otro lado del mar",
                "duration": "23:55"
            },
            {
                "cap": 72,
                "name": "Los hijos del bosque",
                "duration": "23:55"
            }
        ]
        }
}
historial = []
while True:
    menu = input("Bienvenido al programa. Por favor introduzca una opción válida:\n1. Seleccionar una serie\n2. Consultar el historial de vistas\n3. Salir\n->")
    while not menu.isnumeric():
        menu = input("Bienvenido al programa. Por favor introduzca una opción válida:\n1. Seleccionar una serie\n2. Consultar el historial de vistas\n3. Salir\n->")
    else: 
        menu = int(menu)
        if menu == 1:
            vista = {}
            print("Anime Disponibles:")
            n = 0
            for anime_name, seasons in anime.items():
                n+=1
                print("{}. {}".format(n,anime_name))
            anime_input = input("¿Cuál anime le gustaría ver? Por favor introduzca una opción válida:\n->")
            anime_dict = {1: "Demon Slayer", 2: "Spy × Family", 3: "Attack on Titan"}
            if anime_input.isnumeric():
                anime_input = int(anime_input)
                if anime_input in range(1,4):
                    for anime_name, seasons in anime.items():
                        if anime_name == anime_dict[anime_input]:
                            print("Available seasons:")
                            vista["anime_name"]=anime_name
                            for season, list_chapters in seasons.items():
                                print(season)
                            season_input = str(input("¿Cuál temporada desea ver? Por favor introduzca el número de la temporada\n->"))
                            if season_input.isnumeric():
                                for season, list_chapters in seasons.items():
                                    if season_input in season:
                                        vista["season"]=season
                                        print("Available chapters:")
                                        for chapter in list_chapters:
                                            chapter_number = chapter["cap"]
                                            chapter_name = chapter["name"]
                                            chapter_length = chapter["duration"]
                                            print("Chapter number: {}\n\tChapter name: {}\n\tChapter duration: {}".format(chapter_number,chapter_name,chapter_length))
                                        chapter_input = input("¿Cuál capítulo desea ver? Por favor introduzca el número de capítulo:\n->")
                                        if chapter_input.isnumeric():
                                            chapter_input = int(chapter_input)
                                            for chapter in list_chapters:
                                                if chapter_input == chapter["cap"]:
                                                    vista["chapter"]=chapter
            if not vista == {}:
                print("Capítulo seleccionado:")
                for key,value in vista.items():
                    if key == "anime_name" or key == "season":
                        print(key,value)
                    else: 
                        for key,value in value.items():
                            print(key,value)
                historial.append(vista)
        elif menu == 2:
            print("Más reciente")
            for vista in historial: 
                print("\n")
                for key,value in vista.items():
                    if key == "anime_name" or key == "season":
                        print(key,value)
                    else: 
                        for key,value in value.items():
                            print(key,value)
            print("\nMenos reciente\n")
            print("Cantidad de capítulos en el historial: {}\n".format(len(historial)))
        elif menu == 3:
            break
        else:
            continue
import networkx as nx

G = nx.Graph()

U = ["u1", "u2", "u3", "u4", "u5", "u6", "u7"]
F = ["f1", "f2", "f3", "f4", "f5", "f6"]

G.add_nodes_from(U, bipartite=0)
G.add_nodes_from(F, bipartite=1)

edges = [
    ("u1", "f1", 6), ("u1", "f2", 8), ("u1", "f5", 2), ("u1", "f4", 9),
    ("u2", "f2", 10), ("u2", "f3", 3), ("u2", "f5", 6), ("u2", "f6", 7),
    ("u3", "f3", 7), ("u3", "f1", 4), ("u3", "f4", 6),
    ("u4", "f2", 9), ("u4", "f5", 5),
    ("u5", "f1", 7), ("u5", "f6", 6),
    ("u6", "f4", 8), ("u6", "f5", 4),
    ("u7", "f3", 9), ("u7", "f6", 10),
]
for u, f, nota in edges:
    G.add_edge(u, f, weight=nota)

def get_edges(usuario):
    return [f for u, f in G.edges(usuario)]

def cria_usuario(filmes_curtidos):
    U.append("u" + str(len(U) + 1))
    verificar_usuarios_semelhantes(filmes_curtidos)

def verificar_usuarios_semelhantes(filmes_curtidos):
    usuarios_pontos = []
    for usuario in U:
        filmes_avaliados = get_edges(usuario)
        pontos = 0
        for filme in filmes_avaliados:
            if filme in filmes_curtidos:
                edge_data = G.get_edge_data(usuario, filme)
                nota = edge_data['weight']
                pontos += nota if nota >= 6 else nota - 5
        print(usuario + ": " + str(pontos))
        usuarios_pontos.append([usuario, pontos])
    
    top_2 = sorted(usuarios_pontos, key=lambda x: x[1], reverse=True)[:2]
    usuarios_semelhantes = [top_2[0][0], top_2[1][0]]
    
    recomendar_filmes(usuarios_semelhantes, filmes_curtidos)

def recomendar_filmes(usuarios_semelhantes, filmes_curtidos):
    notas_filmes = {}
    for usuario in usuarios_semelhantes:
        filmes_avaliados = get_edges(usuario)
        for filme in filmes_avaliados:
            if filme not in filmes_curtidos:
                edge_data = G.get_edge_data(usuario, filme)
                nota = edge_data['weight']
                if filme not in notas_filmes:
                    notas_filmes[filme] = []
                notas_filmes[filme].append(nota)

    filmes_a_recomendar = []
    for filme, notas in notas_filmes.items():
        media = sum(notas) / len(notas)
        if media >= 6:
            filmes_a_recomendar.append(filme)

    print("Ola " + U[-1] + ". Visto que curtiu os seguintes filmes:")
    print(*filmes_curtidos, sep=',')
    if filmes_a_recomendar:
        print("Para melhor experiencia, recomendamos a voce os seguintes filmes:")
        print(*filmes_a_recomendar, sep=',')
    else:
        print("Não encontramos novas recomendações baseadas nesses gostos.")

    add_edges(filmes_a_recomendar)

def add_edges(filmes_recomendados):
    G.add_node(U[-1])
    for filme in filmes_recomendados:
        G.add_edge(U[-1], filme, recomendado=True)
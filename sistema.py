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
    usuario_novo = "u" + str(len(U) + 1)
    U.append(usuario_novo)
    verificar_usuarios_semelhantes(filmes_curtidos, usuario_novo)
    
def entrar_usuario(usuario):
    filmes_curtidos = []
    filmes = get_edges(usuario)
    for filme in filmes:
        edge_data = G.get_edge_data(usuario, filme)
        nota = edge_data['weight']
        if nota >= 6: 
            filmes_curtidos.append(filme)
    
    verificar_usuarios_semelhantes(filmes_curtidos, usuario)
            
    
def verificar_usuarios_semelhantes(filmes_curtidos, usuario_atual):
    usuarios_pontos = []
    for usuario in U:
        if (usuario != usuario_atual):
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
    
    recomendar_filmes(usuarios_semelhantes, filmes_curtidos, usuario_atual)

def recomendar_filmes(usuarios_semelhantes, filmes_curtidos, usuario_atual):
    notas_filmes = {}
    
    for usuario in usuarios_semelhantes:
        filmes_avaliados = get_edges(usuario)
        for filme in filmes_avaliados:
            if filme not in filmes_curtidos:
                
                edge_data = G.get_edge_data(usuario, filme)
                nota = edge_data['weight']
                if filme not in notas_filmes:
                    notas_filmes[filme] = []
                notas_filmes[filme].append([nota, usuario])

    print(notas_filmes)
    filmes_a_recomendar = []
    for filme, avaliacoes in notas_filmes.items():
        for nota, usuario in avaliacoes: 
            
            # TODO: usar a logica de similaridade: produto(u1, u2) / (notas[u1] * notas[u2]);

            if media >= 6:
                filmes_a_recomendar.append(filme)

    print("Ola " + usuario_atual + ". Visto que curtiu os seguintes filmes:")
    print(*filmes_curtidos, sep=',')
    if filmes_a_recomendar:
        print("Para melhor experiencia, recomendamos a voce os seguintes filmes:")
        print(*filmes_a_recomendar, sep=',')
    else:
        print("Não encontramos novas recomendações baseadas nesses gostos.")

    add_edges(filmes_a_recomendar, usuario_atual)

def add_edges(filmes_recomendados, usuario_atual):
    G.add_node(usuario_atual)
    for filme in filmes_recomendados:
        G.add_edge(usuario_atual, filme, recomendado=True)
import matplotlib.pyplot as plt
import networkx as nx
from sistema import G, F, cria_usuario

filmes_curtidos = []
print('Insira os filmes que voce gostou (x para acabar): ')
while True:
  x = input()
  if x == 'x':
    break
  filmes_curtidos.append(x)

cria_usuario(filmes_curtidos)

# Layout bipartido
pos = nx.bipartite_layout(G, F)

# Cores das arestas (verde se for recomendação)
edge_colors = []
for u, v in G.edges():
    edge_data = G.get_edge_data(u, v)
    if edge_data.get('recomendado'):
        edge_colors.append('green')
    else:
        edge_colors.append('black')

# Desenhar grafo
nx.draw(G, pos, with_labels=True, edge_color=edge_colors, width=3, node_size=1000)

# Mostrar pesos nas arestas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.show()
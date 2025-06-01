import matplotlib.pyplot as plt
import networkx as nx
from sistema import G, F, U, cria_usuario, entrar_usuario

while True:
  print('Olá bem vindo: \n (1) Criar nova conta \n (2) Selecionar uma conta existente')
  escolha = input()
  
  if escolha == '1':
    filmes_curtidos = []
    print('Ola novo usuario, Insira os filmes que voce gostou [f1 - f6] (x para acabar): ')
    while True:
      x = input()
      if x == 'x':
        break
      filmes_curtidos.append(x)
    
    cria_usuario(filmes_curtidos)
    break
    
  elif escolha == '2':
    print('Escolha uma conta para logar [u1 - u7]')
    while True:
      x = input()
      if x not in U: 
        print('Escolha uma conta valida [u1 - u7]')
      else:
        entrar_usuario(x)
        break
    break
  
    
    

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
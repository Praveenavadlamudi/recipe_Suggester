import networkx as nx

SUBS = {"olive oil": ["butter","vegetable oil"], "cheese":["paneer","tofu"]}

def build_graph(recipes):
    G = nx.Graph()
    for r, ingredients in recipes.items():
        G.add_node(r, type="recipe")
        for ing in ingredients:
            G.add_node(ing, type="ingredient")
            G.add_edge(r, ing)
    return G

def greedy_suggest(recipes, available):
    out = []
    for r, ings in recipes.items():
        have = [i for i in ings if i in available]
        missing = [i for i in ings if i not in available]
        score = len(have)/len(ings)
        subs = {m: SUBS[m] for m in missing if m in SUBS}
        out.append({"recipe": r, "have": have, "missing": missing, "substitutions": subs, "score": round(score,2)})
    return sorted(out, key=lambda x: x["score"], reverse=True)
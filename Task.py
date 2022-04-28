
#dfs strategy

graph_tree = {
              "nodes": [       0,
                    1 ,

                   3 , 4,
                              2 ,

                             5 , 6]

           }

stack = []
goal = int(input("enter the goal : "))

def dfs(node):
    for items in graph_tree.values():

        for x in items:


            print(" ", x, end=" --->")

            stack.append(x)

            if x == goal:

                print("\n", "\n", goal, "||", "you've reached the goal")

                break





dfs(goal)

print("\n", "the nodes that has been stored " , "----->",stack)